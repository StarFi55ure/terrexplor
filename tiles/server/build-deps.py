import os
import sh
import shutil
import logging

from sh import wget

SOURCE_CACHE = 'cache'
DOWNLOAD_ARCHIVES = [
    'http://download.osgeo.org/gdal/2.1.1/gdal-2.1.1.tar.xz',
    'http://hash.za.org/files/mapnik-2.2.0.tar.gz'
]

SYSTEM_DEPENDENCIES = [
    # gdal

    'libpq-dev',
    'libgeos-dev',
    'swig',
    'libcfitsio-dev',
    'libhdf5-dev',
    'libkml-dev',
    'libcurl4-gnutls-dev',
    'libpcre3-dev',
    'libqhull-dev',
    'qhull-bin',
    'libfreexl-dev',
    'libxerces-c-dev',
    'libexpat1-dev',
    'liblzma-dev',
    'libjasper-dev',
    'libopenjpeg5',
    'libnetcdf-dev',
    'libogdi3.2-dev',

    # mapnik
    'gcc-4.8',
    'g++-4.8',
    'libcairo2-dev',
    'libtiff5-dev',
    'python-cairo-dev'
]


def process_output(line):
    print(line)


def download_source(url, filename=None):
    if not os.path.exists(SOURCE_CACHE):
        os.makedirs(SOURCE_CACHE)

    if not filename:
        basename = os.path.basename(url)
    else:
        basename = filename

    download_path = os.path.join(SOURCE_CACHE, basename)

    if not os.path.exists(download_path):
        wget(url, c=True, O=download_path, _out=process_output, _err=process_output)


ROOT_DIR = os.getcwd()
BUILD_DEP_DIR = 'build-deps'

# install numpy manually in virtual env
pip = sh.Command('pyenv/bin/pip')
pip.install('numpy', _out=process_output, _err=process_output)

# build library dependencies

############################################################
# gdal
############################################################

BUILD_DEP_DIR = 'build-deps'
if not os.path.exists(BUILD_DEP_DIR):
    os.makedirs(BUILD_DEP_DIR)

os.chdir(BUILD_DEP_DIR)

download_source('http://download.osgeo.org/gdal/2.1.1/gdal-2.1.1.tar.xz')

sh.tar('xf', os.path.join(SOURCE_CACHE, 'gdal-2.1.1.tar.xz'))
os.chdir('gdal-2.1.1')

gdal_configure = sh.Command('./configure')
python_prefix = os.path.abspath('../../pyenv/bin/python')

gdal_configure('--with-python={}'.format(python_prefix), '--with-libtiff=internal', '--with-jpeg=internal', prefix=os.path.abspath('../../pyenv'),
               _out=process_output, _err=process_output)

gdal_make = sh.make
gdal_make(j=8, _out=process_output, _err=process_output)
gdal_make.install(_out=process_output, _err=process_output)


os.chdir(ROOT_DIR)

##############################################################
# Boost
##############################################################

if not os.path.exists(BUILD_DEP_DIR):
    os.makedirs(BUILD_DEP_DIR)

os.chdir(BUILD_DEP_DIR)

print('Downloading boost')
download_source('http://sourceforge.net/projects/boost/files/boost/1.58.0/boost_1_58_0.tar.bz2')

if not os.path.exists('boost_1_58_0'):
    sh.tar('xf', os.path.join(SOURCE_CACHE, 'boost_1_58_0.tar.bz2'))

os.chdir('boost_1_58_0')

bootstrap_sh = sh.Command('./bootstrap.sh')
bootstrap_sh(_out=process_output, _err=process_output)

append_str = 'using python : 2.7 : {};'.format(os.path.abspath('../../pyenv'))
with open('project-config.jam', 'a+') as f:
    for line in f:
        if append_str in line:
            break
    else: # not found
        f.write(append_str)


boost_install_prefix = os.path.abspath('../../pyenv')
b2 = sh.Command('./b2')
b2(j=8, _out=process_output, _err=process_output)
b2('install', prefix=boost_install_prefix)

#################################################################
# Mapnik
#################################################################

os.chdir(ROOT_DIR)
os.chdir(BUILD_DEP_DIR)

print('Downloading mapnik 2.2.0')
download_source('http://hash.za.org/files/mapnik-2.2.0.tar.gz', 'mapnik-2.2.0.tar.gz')

if not os.path.exists('mapnik-2.2.0'):
    sh.tar('xf', os.path.join(SOURCE_CACHE, 'mapnik-2.2.0.tar.gz'))

os.chdir('mapnik-2.2.0')

shutil.copy('../../mapnik-config.py', 'config.py')

build_env = os.environ.copy()
build_env['LD_LIBRARY_PATH'] = os.path.abspath('../../pyenv/lib')

python27 = sh.Command('/usr/bin/python2.7')
python27('scons/scons.py', 'configure', _env=build_env, _out=process_output, _err=process_output)

make = sh.make
make(_env=build_env, _out=process_output, _err=process_output)
make.install(_env=build_env, _out=process_output, _err=process_output)







