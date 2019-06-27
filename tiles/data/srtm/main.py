"""
Process SRTM data to make hillshade rasters
"""
from glob import glob
from shutil import rmtree, copytree

from queue import Queue
import sh
from lxml import etree

from config.config import *
from srtm.hillshadedem import HillshadeDEM


def build_mapnik_theme():
    print('Build mapnik theme')
    if os.path.exists(HILLSHADE_THEME_DIR):
        rmtree(HILLSHADE_THEME_DIR)
    srcdir = os.path.join(SRTM_OUTPUT_DIR, 'hillshade')
    copytree(srcdir, HILLSHADE_THEME_DIR)

    gdalbuildvrt = sh.Command('gdalbuildvrt')
    gdalbuildvrt(os.path.join(HILLSHADE_THEME_DIR, 'hillshade.vrt'), glob(os.path.join(HILLSHADE_THEME_DIR, '*.tiff')))

    Map = etree.Element('Map')
    Map.set('srs', '+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m '
                   '+nadgrids=@null +wktext +no_defs +over')
    Map.set('background-color', '#ffffff')

    parameters = [
        ('bounds', '-180,-85.05112877980659,180,85.05112877980659'),
        ('center', '0,0,2'),
        ('format', 'png8'),
        ('minzoom', '0'),
        ('maxzoom', '22'),
        ('scale', '1'),
        ('name', 'Hillshade Layer')
    ]

    Parameters = etree.SubElement(Map, 'Parameters')
    for n, v in parameters:
        p = etree.SubElement(Parameters, 'Parameter')
        p.set('name', n)
        p.text = v

    Style = etree.SubElement(Map, 'Style')
    Style.set('name', 'raster')

    Rule = etree.SubElement(Style, 'Rule')
    RasterSymbolizer = etree.SubElement(Rule, 'RasterSymbolizer')
    RasterSymbolizer.set('opacity', '1')

    Layer = etree.SubElement(Map, 'Layer')
    Layer.set('name', 'hillshade')
    Layer.set('status', 'on')

    StyleName = etree.SubElement(Layer, 'StyleName')
    StyleName.text = 'raster'

    Datasource = etree.SubElement(Layer, 'Datasource')

    Parameter1 = etree.SubElement(Datasource, 'Parameter')
    Parameter1.set('name', 'type')
    Parameter1.text = etree.CDATA('gdal')

    Parameter2 = etree.SubElement(Datasource, 'Parameter')
    Parameter2.set('name', 'file')
    Parameter2.text = 'hillshade.vrt'

    with open(os.path.join(HILLSHADE_THEME_DIR, 'project.xml'), 'w') as f:
        f.write(str(etree.tostring(Map, pretty_print=True), 'utf-8'))


def main():
    print('Processing SRTM data')
    print('Current directory: {}'.format(os.getcwd()))
    print('SRTM data dir: {}'.format(SRTM_INPUT_DIR))

    processing_queue = Queue()

    bil_zips = glob(SRTM_INPUT_DIR + '/*_bil.zip')
    no_zip = len(bil_zips)
    print('Need to process {} BIL files'.format(no_zip))

    for f in bil_zips:
        print(f)
        processing_queue.put(HillshadeDEM(f, SRTM_OUTPUT_DIR))

    while not processing_queue.empty():
        hillshade = processing_queue.get()
        hillshade.build_hillshade()

    print('Done processing {} BIL files'.format(no_zip))

    build_mapnik_theme()

    if os.path.exists(HILLSHADE_TARGET_THEME_DIR):
        rmtree(HILLSHADE_TARGET_THEME_DIR)
    copytree(HILLSHADE_THEME_DIR, HILLSHADE_TARGET_THEME_DIR)

