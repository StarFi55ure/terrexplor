import os
import sh

from srtm.processors.BaseProcessor import BaseProcessor


class HillshadeProcessor(BaseProcessor):

    def __init__(self, src_file, hillshade_root):
        super(HillshadeProcessor, self).__init__()

        self._src_file = src_file
        self._hillshade_root = hillshade_root

        bn = os.path.splitext(os.path.basename(self._src_file))[0]
        self._final_file = os.path.join(self._hillshade_root, bn + '.tiff')

    def process(self):
        gdaldem_cmd = sh.Command('gdaldem')
        gdaldem = gdaldem_cmd.bake(_out=self.show_progress)

        if not os.path.exists(self._final_file):
            gdaldem.hillshade('-z', '2',
                              '-combined',
                              '-compute_edges',
                              self._src_file, self._final_file)
