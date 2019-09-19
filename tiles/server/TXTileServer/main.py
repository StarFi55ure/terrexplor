import os
import json

import TileStache
from TileStache.Config import buildConfiguration
from flask import Flask
from gunicorn.app.base import BaseApplication
from gunicorn.six import iteritems
from werkzeug.datastructures import Headers
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from mapproxy.wsgiapp import make_wsgi_app

from UPTileServer.api.wsgi import build_wsgi_application
from UPTileServer.dynamictileconfig import DynamicTileConfig

default_app = Flask(__name__)

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
            headers.add("Access-Control-Allow-Origin", "*")
            # headers.add("Access-Control-Allow-Headers", "Origin, ...")
            # headers.add("Access-Control-Allow-Credentials", "true")
            headers.add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
            # headers.add("Access-Control-Expose-Headers", "...")
            return start_response(status, headers.to_list(), exc_info)

        if environ.get("REQUEST_METHOD") == "OPTIONS":
            add_cors_headers("200 Ok", [("Content-Type", "text/plain")])
            return [b'200 Ok']

        return self.app(environ, add_cors_headers)


class GunicornApplication(BaseApplication):
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


def get_tilestache_config():
    if os.path.exists('tilestache.cfg'):
        with open('tilestache.cfg', 'r') as f:
            config_data = json.load(f)
        return config_data

    raise Exception("No configuration file set")


def get_gunicorn_config():
    options = {
        'bind': 'localhost:6789',
        'workers': 4,
        'worker_class': 'gevent',
        'max_requests': 1000
    }

    return options


def main():
    print('Starting UPlanet tile server.')
    # setup tilestache for serving tiles

    tilestache_config_json = get_tilestache_config()
    static_tilestache_config = buildConfiguration(tilestache_config_json)
    tilestache_config = DynamicTileConfig(static_tilestache_config)
    tile_app = TileStache.WSGITileServer(tilestache_config)
    #tile_app = make_wsgi_app('mapproxy.yaml/mapproxy.yaml')

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
        'http://localhost:7000',
        'http://tiles.urbanplanet.local',
        'http://urbanplanet.local',
        'http://urbanplanet.dyndns.org'
    ])

    if 'UP_RUN_MODE' in os.environ and os.environ['UP_RUN_MODE'] == 'production':
        # run everything through Gunicorn
        gunicorn_options = get_gunicorn_config()
        gunicorn_app = GunicornApplication(app, gunicorn_options)
        gunicorn_app.run()
    else:
        run_simple('0.0.0.0', 6789, app, use_reloader=True)


if __name__ == '__main__':
    main()