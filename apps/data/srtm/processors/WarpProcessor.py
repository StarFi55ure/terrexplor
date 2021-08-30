import os
import sh

from srtm.processors.BaseProcessor import BaseProcessor


class WarpProcessor(BaseProcessor):

    def __init__(self, src_file, warp_root):
        super(WarpProcessor, self).__init__()

        self._src_file = src_file
        self._warp_root = warp_root

        bn = os.path.splitext(os.path.basename(self._src_file))[0]
        self._final_file = os.path.join(self._warp_root, bn + '.tiff')

    def process(self):
        gdalwarp_cmd = sh.Command('gdalwarp')
        gdalwarp = gdalwarp_cmd.bake(
            '-of', 'GTiff',
            '-co', 'TILED=YES',
            # '-srcnodata', '32767',
            '-t_srs', '+proj=merc +ellps=sphere +R=6378137 +a=6378137 +units=m',
            #'-rcs',
            #'-order', '3',
            #'-tr', '30', '30',
            #'-ts', '3000', '0',
            #'-wt', 'Float32',
            #'-ot', 'Float32',
            '-wo', 'SAMPLE_STEPS=1000',
            '-r', 'bilinear',
            # '-multi',
            _out=self.show_progress)

        if not os.path.exists(self._final_file):
            gdalwarp(self._src_file, self._final_file)
