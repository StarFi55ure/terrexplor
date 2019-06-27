import os
import sh

from srtm.processors.BaseProcessor import BaseProcessor


class ConvertToGeoTIFFProcessor(BaseProcessor):

    def __init__(self, bil_file, convert_root):
        super(ConvertToGeoTIFFProcessor, self).__init__()

        self._bil_file = bil_file
        self._convert_root = convert_root

        bn = os.path.splitext(os.path.basename(self._bil_file))[0]
        self._final_file = os.path.join(self._convert_root, bn + '.tiff')

    def process(self):
        gdal_translate_cmd = sh.Command('gdal_translate')
        gdal_translate = gdal_translate_cmd.bake(
            '-of', 'GTiff',
            '-co', 'TILED=YES',
            #'-a_srs', '+proj=latlong',
            _out=self.show_progress)

        if not os.path.exists(self._final_file):
            #adapted_file = os.path.join('output/adapted', src_basename_tif)
            gdal_translate(self._bil_file, self._final_file)

