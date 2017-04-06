import subprocess
import glob
import os

tile_list = ['00N_100E']

for tile_name in tile_list:

    # download tcd tile
    extent_url = r'http://commondatastorage.googleapis.com/earthenginepartners-hansen/GFC2014/Hansen_GFC2014_treecover2000_{}.tif'.format(tile_name)

    extent_local = '{}.tif'.format(tile_name)

    subprocess.check_call(['wget', '-O', extent_local, extent_url])

    # mask tcd tile
    masked_tile_30 = '{}_masked.tif'.format(tile_name)
    cmd = ['gdal_calc.py', '-A', extent_local, '--outfile={}'.format(masked_tile_30), '--calc=A>30', '--NoDataValue=0', '--co', 'COMPRESS=LZW']
    subprocess.check_call(cmd)

    # polygonize tile
    polygonize_cmd = ['./test.sh', '-m', 'parallel', masked_tile_30]
    subprocess.check_call(polygonize_cmd)

    # merge the tile
    combine_cmd = ['./combine.sh']
    subprocess.check_call(combine_cmd)

    # zip the tile
    merge_shape_list = glob.glob('merge.*')
    zipped_tile = '{}.zip'.format(tile_name)
    zip_cmd = ['zip', zipped_tile] +  merge_shape_list
    subprocess.check_call(zip_cmd)

    # upload to s3
    upload_cmd = ['aws', 's3', 'cp', zipped_tile, 's3://gfw-files/sam/']
    subprocess.check_call(upload_cmd)

    # clean directory
    files_to_remove = [extent_local, masked_tile_30, zipped_tile] + merge_shape_list
    for file in files_to_remove:
        os.remove(file)
