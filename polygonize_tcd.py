import subprocess

tile_list = ['00N_000E']

for tile_name in tile_list:

    # download tcd tile
    extent_url = r'http://commondatastorage.googleapis.com/earthenginepartners-hansen/GFC2014/Hansen_GFC2014_treecover2000_{}.tif'.format(tile_name)
    
    extent_local = r'/home/ubuntu/{}.tif'.format(tile_name)
    
    subprocess.check_call(['wget', '-O', extent_local, extent_url])
    
    # mask tcd tile
    masked_tile_30 = '--outfile={}_masked.tif'.format(tile_name)
    cmd = [r'C:\Program Files\GDAL\gdal_calc.py', '-A', input_tif, outfile, '--calc="A>30"', '--NoDataValue=0', '-co', 'COMPRESS=LZW']
    subprocess.check_call(cmd)
    
    # polygonize tile
    polygonize_cmd = ['./test.sh', '-m', 'parallel', masked_tile_30]
    subprocess.check_call(polygonize_cmd)