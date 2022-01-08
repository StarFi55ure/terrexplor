import os
from pip._vendor.distlib.compat import ZipFile

from srtm.processors.BaseProcessor import BaseProcessor


class BILExtractorProcessor(BaseProcessor):

    def __init__(self, zip_file, output_root):
        super(BILExtractorProcessor, self).__init__()

        self._zip_file = zip_file
        self._output_root = output_root

        bn = os.path.splitext(os.path.basename(self._zip_file))[0][:-4]
        self._final_file = os.path.join(self._output_root, bn + '.bil')

    def process(self):

        if not os.path.exists(self._final_file):
            f = ZipFile(self._zip_file)
            f.extractall(self._output_root)

