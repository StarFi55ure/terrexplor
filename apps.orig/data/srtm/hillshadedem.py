import os

from srtm.processors.BILExtractorProcessor import BILExtractorProcessor
from srtm.processors.ConvertToGeoTIFFProcessor import ConvertToGeoTIFFProcessor
from srtm.processors.HillshadeProcessor import HillshadeProcessor
from srtm.processors.WarpProcessor import WarpProcessor


class HillshadeDEM:
    """
    Process a bil file into a hillshade GeoTIFF
    """

    def __init__(self, src_file, output_dir):
        self._src_file = src_file
        self._output_dir = output_dir

    def build_hillshade(self):
        print('processing file {}'.format(self._src_file))

        # extract zip files
        bil_file = self.extract_src_file()
        converted_file = self.convert_to_geotiff(bil_file)
        warped_file = self.warp_file(converted_file)

        # self.convert_to_denoise_grid()
        # self.denoise()
        # self.warp_back_to_geotiff()
        # self.create_slopeshade()
        self.create_hillshade(warped_file)

    def extract_src_file(self):
        print('extracting bil files for: {}'.format(self._src_file))
        extract_root = os.path.join(self._output_dir, 'extract')
        if not os.path.exists(extract_root):
            os.makedirs(extract_root)
        extractor = BILExtractorProcessor(self._src_file, extract_root)
        extractor.process()

        return extractor.final_file

    def convert_to_geotiff(self, bil_file):
        print('converting bil file: {}'.format(bil_file))
        convert_root = os.path.join(self._output_dir, 'convert')
        if not os.path.exists(convert_root):
            os.makedirs(convert_root)

        converter = ConvertToGeoTIFFProcessor(bil_file, convert_root)
        converter.process()

        return converter.final_file

    def warp_file(self, converted_file):
        print('warping converted file: {}'.format(converted_file))
        warp_root = os.path.join(self._output_dir, 'warped')
        if not os.path.exists(warp_root):
            os.makedirs(warp_root)

        warper = WarpProcessor(converted_file, warp_root)
        warper.process()

        return warper.final_file

    # def convert_to_denoise_grid(self):
    #     pass
    #
    # def denoise(self):
    #     pass
    #
    # def warp_back_to_geotiff(self):
    #     pass
    #
    # def create_slopeshade(self):
    #     pass

    def create_hillshade(self, warped_file):
        print('creating hillshade: {}'.format(warped_file))
        hillshade_root = os.path.join(self._output_dir, 'hillshade')

        if not os.path.exists(hillshade_root):
            os.makedirs(hillshade_root)

        hillshader = HillshadeProcessor(warped_file, hillshade_root)
        hillshader.process()

        return hillshader.final_file
