import os
import shutil
import tarfile

from setuptools import setup, find_packages, Command

from TXTileServer.config import SOFTWARE_VERSION

PACKAGE_NAME = 'terrexplor-tile-server'

all_packages = find_packages()
final_package_data = {}
final_package_dir = {}
final_data_files = []


class DebifyCommand(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        zipbasename = '{}-{}'.format(PACKAGE_NAME, SOFTWARE_VERSION)
        zipname = os.path.join('dist', zipbasename + '.tar.gz')

        debzipname = os.path.join('dist', zipbasename + '.orig.tar.gz')

        with tarfile.open(zipname, 'r|gz') as tar:
            tar.extractall('dist')

        shutil.copytree('debian', os.path.join('dist', zipbasename, 'debian'))
        # shutil.copyfile(zipname, debzipname)
        # with ZipFile(debzipname, 'w') as debzip:
        #     debzip.write('debian')

        with tarfile.open(debzipname, 'w|gz') as debtar:
            debtar.add(os.path.join('dist', zipbasename), zipbasename)

        shutil.rmtree((os.path.join('dist', zipbasename)))
        pass


def bundle_mapproxy_configs():
    global final_package_data

    final_package_data.update({
        'TXTileServer.config.mapproxy': [
            '*.yaml'
        ]
    })


def bundle_themes():
    global final_package_data

    final_package_data.update({
        'TXTileServer.themes': [
            'terrexplor-main/*',
            'terrexplor-main/fonts/*',
            'terrexplor-main/img/*',
            'terrexplor-main/res/*'
        ]
    })


if __name__ == '__main__':
    bundle_mapproxy_configs()
    bundle_themes()

    setup(
        name=PACKAGE_NAME,
        author='Julian Kennedy',
        author_email='juliankenn@gmail.com',

        include_package_data=True,

        version=SOFTWARE_VERSION,

        package_data=final_package_data,
        package_dir=final_package_dir,

        packages=all_packages,

        install_requires=[
            'flask==1.0.2',
            'flask_restful',
            'gunicorn',
            'gevent',
            'sh',
            'ipython',
            'requests',
            'mapproxy',
            'werkzeug==0.14.1'
        ],

        entry_points={
            'console_scripts': [
                'tx-tile-server = TXTileServer.main:main'
            ]
        },

        cmdclass={
            'sdist_debify': DebifyCommand
        }

    )
