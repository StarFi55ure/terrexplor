import json
import os
import shutil
from abc import ABC
import yaml
import copy
import tempfile
from lxml import etree

from flask import Flask
from gunicorn.app.base import BaseApplication
from gunicorn.six import iteritems
from pkg_resources import resource_filename, resource_string
from werkzeug.datastructures import Headers
from werkzeug.debug import DebuggedApplication
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from mapproxy.wsgiapp import make_wsgi_app

from TXTileServer.api.wsgi import build_wsgi_application
from TXTileServer.dynamictileconfig import DynamicTileConfig

default_app = Flask(__name__)
default_app.debug = True

exit_data = None

@default_app.route('/')
def index():
    return "Nothing here"


class CORSMiddleware(object):
    """Add Cross-origin resource sharing headers to every request."""

    def __init__(self, app, origins):
        self.app = app
        self.origins = origins

    def __call__(self, environ, start_response):
        def add_cors_headers(status, headers, exc_info=None):
            headers = Headers(headers)

            # for origin in self.origins:
            headers.set("Access-Control-Allow-Origin", "*")
            # headers.add("Access-Control-Allow-Headers", "Origin, ...")
            # headers.add("Access-Control-Allow-Credentials", "true")
            headers.add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
            # headers.add("Access-Control-Expose-Headers", "...")
            return start_response(status, [h for h in headers], exc_info)

        if environ.get("REQUEST_METHOD") == "OPTIONS":
            add_cors_headers("200 Ok", [("Content-Type", "text/plain")])
            return [b'200 Ok']

        return self.app(environ, add_cors_headers)


class GunicornApplication(BaseApplication, ABC):
    """
    This class represents the Gunicorn wsgi application
    """

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(GunicornApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def get_gunicorn_config():
    options = {
        'bind': 'localhost:6789',
        'workers': 4,
        'worker_class': 'gevent',
        'max_requests': 100,

        'on_exit': on_exit
    }

    return options


def build_runtime_theme(theme_file):
    print("Orig theme: {}".format(theme_file))
    if 'TX_RUN_MODE' in os.environ and os.environ['TX_RUN_MODE'] == 'prod':
        DBNAME = 'terrexplor'
        DBUSER = 'terrexplor'
        DBPASSWORD = 'hmlDmfYzg0B2LYbgHFUj5z3MtO8='
        DBHOST = '172.20.1.30'
    else:
        DBNAME = 'terrexplor'
        DBUSER = 'terrexplor'
        DBPASSWORD = 'terrexplor'
        DBHOST = 'localhost'

    # copy theme to temporary directory
    tdir = tempfile.mkdtemp()
    rundir = os.path.join(tdir, 'theme')
    print("Using theme dir: {}".format(rundir))
    theme_orig_dir, theme_orig_file = os.path.split(theme_file)
    shutil.copytree(theme_orig_dir, rundir)

    # update datasources
    print("Runtim XML file: {}".format(os.path.join(rundir, theme_orig_file)))
    with open(os.path.join(rundir, theme_orig_file), 'r') as f:
        xml_data = etree.parse(f)

    datasources = xml_data.xpath('/Map/Layer/Datasource')
    print(len(datasources))

    for datasource in datasources:
        datasource.xpath("Parameter[@name='dbname']")[0].text = etree.CDATA(DBNAME)
        datasource.xpath("Parameter[@name='user']")[0].text = etree.CDATA(DBUSER)
        datasource.xpath("Parameter[@name='password']")[0].text = etree.CDATA(DBPASSWORD)
        datasource.xpath("Parameter[@name='host']")[0].text = etree.CDATA(DBHOST)

    # create runtime theme file
    _, tfile = tempfile.mkstemp(dir=rundir)
    print('Created temp theme file {}'.format(tfile))
    with open(tfile, 'wb') as f:
        f.write(etree.tostring(xml_data, pretty_print=4))

    return tdir, tfile


def get_mapproxy_configfile():
    base_mapproxy_yaml = resource_string('TXTileServer.config.mapproxy', 'mapproxy.yaml')

    data = yaml.load(base_mapproxy_yaml)
    new_data = copy.deepcopy(data)

    temp_theme_files = []
    for key in data['sources']:
        s = data['sources'][key]
        if s['type'] == 'mapnik':
            theme_name = s['mapfile']
            theme_path = resource_filename('TXTileServer', 'themes')
            final_runtime_dir, final_theme_file = build_runtime_theme(os.path.join(theme_path, theme_name))
            temp_theme_files.append({
                'dir': final_runtime_dir,
                'tfile': final_theme_file
            })
            ns = new_data['sources'][key]
            ns['mapfile'] = final_theme_file

    _, pfile = tempfile.mkstemp()
    with open(pfile, 'w') as f:
        f.write(yaml.dump(new_data))

    return pfile, temp_theme_files


def on_exit(server):
    print("Cleanup before exiting")
    if exit_data:
        print("Unlinking mapproxy")
        os.unlink(exit_data['mapproxy_config'])
        for f in exit_data['tempdirs']:
            # TODO: must delete directory as well
            print("rm tree {}".format(f['dir']))
            shutil.rmtree(f['dir'])


def main():
    global exit_data

    print('Starting TerreXplor Tile Server.')

    # setup mapproxy for serving tiles
    mapproxy_config_file, temp_theme_files = get_mapproxy_configfile()

    print("Mapproxy file {}".format(mapproxy_config_file))
    tile_app = make_wsgi_app(mapproxy_config_file)

    # setup api app for ingesting data
    api_app = build_wsgi_application()

    # setup dispatcher to run tilestache and api at same time
    app = DispatcherMiddleware(default_app, {
        '/tiles': tile_app,
        '/api': api_app
    })

    # setup CORS to allow cross domain requests
    app = CORSMiddleware(app, [
        'http://localhost:8080',
        'http://localhost:7000'
    ])

    gunicorn_options = get_gunicorn_config()

    if 'TX_RUN_MODE' in os.environ and os.environ['TX_RUN_MODE'] == 'prod':
        # run everything through Gunicorn
        final_app = app
    else:
        final_app = app
        gunicorn_options['max_requests'] = 0

    # save this for exit function later on
    exit_data = {
        'mapproxy_config': mapproxy_config_file,
        'tempdirs': temp_theme_files
    }

    gunicorn_app = GunicornApplication(final_app, gunicorn_options)
    gunicorn_app.run()


if __name__ == '__main__':
    main()
