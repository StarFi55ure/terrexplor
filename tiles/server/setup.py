from setuptools import setup, find_packages

setup(
    name='TXTileServer',
    author='Julian Kennedy',
    author_email='juliankenn@gmail.com',

    version='0.0.1',

    packages=find_packages(),
    install_requires=[
        'flask',
        'flask_restful',
        'gunicorn',
        'gevent',
        'watchdog',
        'sh',
        'ipython',
        'numpy',
        'arrow',
        'requests',
        'mapproxy',
        'celery'
    ],

    entry_points={
        'console_scripts': [
            'runserver = TXTileServer.main:main'
        ]
    }

)
