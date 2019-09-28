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

        version=SOFTWARE_VERSION,

        package_data=final_package_data,
        package_dir=final_package_dir,

        packages=all_packages,

        install_requires=[
            'flask',
            'flask_restful',
            'gunicorn',
            'gevent',
            'sh',
            'ipython',
            'arrow',
            'requests',
            'mapproxy',
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
