from setuptools import setup, find_packages

setup(
    name='DataProcessing',
    author='Julian Kennedy',

    install_requires=[
        'sh',
        'numpy',
        'lxml'
    ],

    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'process_srtm_data = srtm.main:main'
        ]
    }
)
