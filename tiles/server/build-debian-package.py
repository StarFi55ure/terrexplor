import os
import tempfile
import shutil
import sh
from glob import glob

ROOT_DIR = os.getcwd()

TMP_DIR = tempfile.mkdtemp()
print('Working in: {}'.format(TMP_DIR))

INSTALL_DIR = os.path.join(TMP_DIR, 'opt/urbanplanet/tileserver')
CONFIG_DIR = os.path.join(TMP_DIR, 'etc/tileserver')
CACHE_DIR = os.path.join(TMP_DIR, 'var/cache/tileserver/cache')

os.makedirs(INSTALL_DIR)
os.makedirs(CONFIG_DIR)
os.makedirs(CACHE_DIR)

shutil.copytree(os.path.abspath('pyenv'),
        os.path.join(INSTALL_DIR, 'pyenv'))

shutil.copytree(os.path.abspath('themes'),
        os.path.join(CONFIG_DIR, 'themes'))

shutil.copyfile(os.path.abspath('tilestache-prod.cfg'),
           os.path.join(CONFIG_DIR, 'tilestache.cfg'))

print(sh.ls(TMP_DIR))

os.chdir(TMP_DIR)

fpm = sh.fpm
fpm = fpm.bake(s='dir', t='deb', n='up-tileserver', v='0.0.1')
fpm('opt', 'etc', 'var')


os.chdir(ROOT_DIR)
deb_files = glob(TMP_DIR + '/*.deb')
print deb_files

for deb in deb_files:
    shutil.copy(deb, ROOT_DIR)

shutil.rmtree(TMP_DIR)

