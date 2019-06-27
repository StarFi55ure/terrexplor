#!/usr/bin/env python
import os
import threading
from queue import Queue

import sh

gdal_translate_cmd = sh.Command('gdal_translate')
gdalwarp_cmd = sh.Command('gdalwarp')
gdaldem_cmd = sh.Command('gdaldem')
mdenoise = sh.Command('mdenoise')


def show_progress(line):
    print(line)


gdal_translate = gdal_translate_cmd.bake(
    '-of', 'GTiff',
    '-co', 'TILED=YES',
    #'-a_srs', '+proj=latlong',
    _out=show_progress)

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
    _out=show_progress)

gdaldem = gdaldem_cmd.bake(_out=show_progress)

print(gdal_translate)
print(gdalwarp)
print(gdaldem)

for p in ['adapted', 'warped', 'grid', 'griddn', 'warpeddn', 'hillshade', 'slopeshade']:
    d = os.path.join('output', p)
    if not os.path.exists(d):
        os.makedirs(d)

files = sh.glob('input/*_v3.bil')

# files = [f for f in files if 's34_e018' in f]
print(files)


def process_file(queue):
   while not queue.empty():
        src_bil_file = queue.get()
        print('processing file: ' + src_bil_file)

        src_basename = os.path.basename(src_bil_file)
        src_basename_tif = os.path.splitext(src_basename)[0] + '.tif'

        if os.path.exists(os.path.join('output/hillshade', src_basename_tif)):
            continue

        # adapted - make sure srs in included in file and convert to GeoTIFF
        print('adapt')
        adapted_file = os.path.join('output/adapted', src_basename_tif)
        gdal_translate(src_bil_file, adapted_file)

        # warped
        print('warp')
        warped_file = os.path.join('output/warped', src_basename_tif)
        gdalwarp(adapted_file, warped_file)

        # # warp to grid
        # grid_file_name = os.path.splitext(src_basename)[0] + '.asc'
        # grid_file = os.path.join('output/grid', grid_file_name)
        # gdal_translate_cmd('-of', 'AAIGrid',
        #                    warped_file, grid_file)
        #
        # # denoise
        # print('denoise')
        # griddn_file_name = os.path.splitext(src_basename)[0] + '_dn.asc'
        # griddn_file = os.path.join('output/griddn', griddn_file_name)
        # mdenoise('-i', grid_file,
        #          '-n', '5',
        #          '-t', '0.99',
        #          '-o', griddn_file
        #          )
        #
        # # warp back to tiff
        # warpeddn_file = os.path.join('output/warpeddn', src_basename_tif)
        # gdal_translate_cmd('-of', 'GTiff',
        #                    griddn_file, warpeddn_file)

        # slopeshade
        # print('slopeshade')
        ##slope file contains slope data
        # slope_file = '{}_slope.tif'.format(src_basename.split('.')[0])
        # slope_file = os.path.join('output/slopeshade', slope_file)
        ## shade file gets used by mapnik
        # slopeshade_file = os.path.join('output/slopeshade', src_basename_tif)

        # gdaldem.slope(warped_file, slope_file)
        # gdaldem('color-relief', slope_file, 'slope-ramp.txt', slopeshade_file)


        # hillshade (needs to work on a merged file)
        print('hillshade')
        hillshade_file = os.path.join('output/hillshade', src_basename_tif)
        gdaldem.hillshade('-z', '2',
                          '-combined',
                          '-compute_edges',
                          warped_file, hillshade_file)


job_queue = Queue()

for src_bil_file in files:
    job_queue.put(src_bil_file)

threads = []
for i in range(8):
    t = threading.Thread(target=process_file, args=(job_queue,))
    threads.append(t)
    t.start()
