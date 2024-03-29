import os

DATA_DIR = 'raster/srtm'
MAPNIK_THEME_DIR = 'raster/mapnik'

SRTM_INPUT_DIR = os.path.join(DATA_DIR, 'input')
SRTM_OUTPUT_DIR = os.path.join(DATA_DIR, 'output')

HILLSHADE_THEME_DIR = os.path.join(MAPNIK_THEME_DIR, 'hillshade')

HILLSHADE_TARGET_THEME_DIR = '../server/themes/hillshade-built-layer'

