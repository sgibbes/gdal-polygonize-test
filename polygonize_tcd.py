import subprocess

tile_list = ['00N_000E']

for tile_name in tile_list:

    # download tcd tile
    extent_url = r'http://commondatastorage.googleapis.com/earthenginepartners-hansen/GFC2014/Hansen_GFC2014_treecover2000_{}.tif'.format(tile_name)

    extent_local = r'/home/ubuntu/{}.tif'.format(tile_name)

   # subprocess.check_call(['wget', '-O', extent_local, extent_url])

    # mask tcd tile
    masked_tile_30 = '{}_masked.tif'.format(tile_name)
    cmd = ['gdal_calc.py', '-A', extent_local, masked_tile_30, '--calc=A>30', '--NoDataValue=0', '--co', 'COMPRESS=LZW']

    #subprocess.check_call(cmd)

    # polygonize tile
    polygonize_cmd = ['./test.sh', '-m', 'parallel', masked_tile_30]
    #subprocess.check_call(polygonize_cmd)

    # merge the tile
    merge_cmd = ['./merge.sh']
    #subprocess.check_call(merge_cmd)

    # zip the tile
    zipped_tile = '~/gdal-polygonize-test/{}.zip'.format(tile_name)
    zip_cmd = ['zip', zipped_tile, 'merge*']
    print zip_cmd
    subprocess.check_call(zip_cmd)

    # upload to s3
    upload_cmd = ['aws', 's3', 'cp', zipped_tile, 's3://gfw-files/sam/']

    # clean directory
    file_to_rm = ['merged*', '*.tif']
    for file in file_to_rm:
        rm_cmd = ['rm', 'file']
        subprocess.check_call(rm_cmd)
