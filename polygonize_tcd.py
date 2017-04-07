import subprocess
import glob
import os
from osgeo import ogr

tile_list= ['00N_070E', '00N_070W', '00N_080E', '00N_080W', '00N_090E', '00N_090W', '00N_100E', '00N_100W', '00N_110E', '00N_110W', '00N_120E', '00N_120W', '00N_130E', '00N_130W', '00N_140E', '00N_140W', '00N_150E', '00N_150W', '00N_160E', '00N_160W', '00N_170E', '00N_170W', '00N_180W', '10N_000E', '10N_010E', '10N_010W', '10N_020E', '10N_020W', '10N_030E', '10N_030W', '10N_040E', '10N_040W', '10N_050E', '10N_050W', '10N_060E', '10N_060W', '10N_070E', '10N_070W', '10N_080E', '10N_080W', '10N_090E', '10N_090W', '10N_100E', '10N_100W', '10N_110E', '10N_110W', '10N_120E', '10N_120W', '10N_130E', '10N_130W', '10N_140E', '10N_140W', '10N_150E', '10N_150W', '10N_160E', '10N_160W', '10N_170E', '10N_170W', '10N_180W', '10S_000E', '10S_010E', '10S_010W', '10S_020E', '10S_020W', '10S_030E', '10S_030W', '10S_040E', '10S_040W', '10S_050E', '10S_050W', '10S_060E', '10S_060W', '10S_070E', '10S_070W', '10S_080E', '10S_080W', '10S_090E', '10S_090W', '10S_100E', '10S_100W', '10S_110E', '10S_110W', '10S_120E', '10S_120W', '10S_130E', '10S_130W', '10S_140E', '10S_140W', '10S_150E', '10S_150W', '10S_160E', '10S_160W', '10S_170E', '10S_170W', '10S_180W', '20N_000E', '20N_010E', '20N_010W', '20N_020E', '20N_020W', '20N_030E', '20N_030W', '20N_040E', '20N_040W', '20N_050E', '20N_050W', '20N_060E', '20N_060W', '20N_070E', '20N_070W', '20N_080E', '20N_080W', '20N_090E', '20N_090W', '20N_100E', '20N_100W', '20N_110E', '20N_110W', '20N_120E', '20N_120W', '20N_130E', '20N_130W', '20N_140E', '20N_140W', '20N_150E', '20N_150W', '20N_160E', '20N_160W', '20N_170E', '20N_170W', '20N_180W', '20S_000E', '20S_010E', '20S_010W', '20S_020E', '20S_020W', '20S_030E', '20S_030W', '20S_040E', '20S_040W', '20S_050E', '20S_050W', '20S_060E', '20S_060W', '20S_070E', '20S_070W', '20S_080E', '20S_080W', '20S_090E', '20S_090W', '20S_100E', '20S_100W', '20S_110E', '20S_110W', '20S_120E', '20S_120W', '20S_130E', '20S_130W', '20S_140E', '20S_140W', '20S_150E', '20S_150W', '20S_160E', '20S_160W', '20S_170E', '20S_170W', '20S_180W', '30N_000E', '30N_010E', '30N_010W', '30N_020E', '30N_020W', '30N_030E', '30N_030W', '30N_040E', '30N_040W', '30N_050E', '30N_050W', '30N_060E', '30N_060W', '30N_070E', '30N_070W', '30N_080E', '30N_080W', '30N_090E', '30N_090W', '30N_100E', '30N_100W', '30N_110E', '30N_110W', '30N_120E', '30N_120W', '30N_130E', '30N_130W', '30N_140E', '30N_140W', '30N_150E', '30N_150W', '30N_160E', '30N_160W', '30N_170E', '30N_170W', '30N_180W', '30S_000E', '30S_010E', '30S_010W', '30S_020E', '30S_020W', '30S_030E', '30S_030W', '30S_040E', '30S_040W', '30S_050E', '30S_050W', '30S_060E', '30S_060W', '30S_070E', '30S_070W', '30S_080E', '30S_080W', '30S_090E', '30S_090W', '30S_100E', '30S_100W', '30S_110E', '30S_110W', '30S_120E', '30S_120W', '30S_130E', '30S_130W', '30S_140E', '30S_140W', '30S_150E', '30S_150W', '30S_160E', '30S_160W', '30S_170E', '30S_170W', '30S_180W', '40N_000E', '40N_010E', '40N_010W', '40N_020E', '40N_020W', '40N_030E', '40N_030W', '40N_040E', '40N_040W', '40N_050E', '40N_050W', '40N_060E', '40N_060W', '40N_070E', '40N_070W', '40N_080E', '40N_080W', '40N_090E', '40N_090W', '40N_100E', '40N_100W', '40N_110E', '40N_110W', '40N_120E', '40N_120W', '40N_130E', '40N_130W', '40N_140E', '40N_140W', '40N_150E', '40N_150W', '40N_160E', '40N_160W', '40N_170E', '40N_170W', '40N_180W', '40S_000E', '40S_010E', '40S_010W', '40S_020E', '40S_020W', '40S_030E', '40S_030W', '40S_040E', '40S_040W', '40S_050E', '40S_050W', '40S_060E', '40S_060W', '40S_070E', '40S_070W', '40S_080E', '40S_080W', '40S_090E', '40S_090W', '40S_100E', '40S_100W', '40S_110E', '40S_110W', '40S_120E', '40S_120W', '40S_130E', '40S_130W', '40S_140E', '40S_140W', '40S_150E', '40S_150W', '40S_160E', '40S_160W', '40S_170E', '40S_170W', '40S_180W', '50N_000E', '50N_010E', '50N_010W', '50N_020E', '50N_020W', '50N_030E', '50N_030W', '50N_040E', '50N_040W', '50N_050E', '50N_050W', '50N_060E', '50N_060W', '50N_070E', '50N_070W', '50N_080E', '50N_080W', '50N_090E', '50N_090W', '50N_100E', '50N_100W', '50N_110E', '50N_110W', '50N_120E', '50N_120W', '50N_130E', '50N_130W', '50N_140E', '50N_140W', '50N_150E', '50N_150W', '50N_160E', '50N_160W', '50N_170E', '50N_170W', '50N_180W', '50S_000E', '50S_010E', '50S_010W', '50S_020E', '50S_020W', '50S_030E', '50S_030W', '50S_040E', '50S_040W', '50S_050E', '50S_050W', '50S_060E', '50S_060W', '50S_070E', '50S_070W', '50S_080E', '50S_080W', '50S_090E', '50S_090W', '50S_100E', '50S_100W', '50S_110E', '50S_110W', '50S_120E', '50S_120W', '50S_130E', '50S_130W', '50S_140E', '50S_140W', '50S_150E', '50S_150W', '50S_160E', '50S_160W', '50S_170E', '50S_170W', '50S_180W', '60N_000E', '60N_010E', '60N_010W', '60N_020E', '60N_020W', '60N_030E', '60N_030W', '60N_040E', '60N_040W', '60N_050E', '60N_050W', '60N_060E', '60N_060W', '60N_070E', '60N_070W', '60N_080E', '60N_080W', '60N_090E', '60N_090W', '60N_100E', '60N_100W', '60N_110E', '60N_110W', '60N_120E', '60N_120W', '60N_130E', '60N_130W', '60N_140E', '60N_140W', '60N_150E', '60N_150W', '60N_160E', '60N_160W', '60N_170E', '60N_170W', '60N_180W', '70N_000E', '70N_010E', '70N_010W', '70N_020E', '70N_020W', '70N_030E', '70N_030W', '70N_040E', '70N_040W', '70N_050E', '70N_050W', '70N_060E', '70N_060W', '70N_070E', '70N_070W', '70N_080E', '70N_080W', '70N_090E', '70N_090W', '70N_100E', '70N_100W', '70N_110E', '70N_110W', '70N_120E', '70N_120W', '70N_130E', '70N_130W', '70N_140E', '70N_140W', '70N_150E', '70N_150W', '70N_160E', '70N_160W', '70N_170E', '70N_170W', '70N_180W', '80N_000E', '80N_010E', '80N_010W', '80N_020E', '80N_020W', '80N_030E', '80N_030W', '80N_040E', '80N_040W', '80N_050E', '80N_050W', '80N_060E', '80N_060W', '80N_070E', '80N_070W', '80N_080E', '80N_080W', '80N_090E', '80N_090W', '80N_100E', '80N_100W', '80N_110E', '80N_110W', '80N_120E', '80N_120W', '80N_130E', '80N_130W', '80N_140E', '80N_140W', '80N_150E', '80N_150W', '80N_160E', '80N_160W', '80N_170E', '80N_170W', '80N_180W']
#tile_list = ['50S_120W', '00N_000E']
for tile_name in tile_list:

    # download tcd tile
    extent_url = r'http://commondatastorage.googleapis.com/earthenginepartners-hansen/GFC2014/Hansen_GFC2014_treecover2000_{}.tif'.format(tile_name)
    extent_local = '{}.tif'.format(tile_name)
    subprocess.check_call(['wget', '-O', extent_local, extent_url])

    # resample tile to .00075 (3x bigger pixels)
    resample_tile = '{}_resample.tif'.format(tile_name)
    resample_cmd = ['gdal_translate', '-r', 'nearest', '-tr', '.00075', '.00075', '-co', 'COMPRESS=LZW', extent_local, resample_tile]
    subprocess.check_call(resample_cmd)

    # mask tcd tile
    masked_tile_30 = '{}_masked.tif'.format(tile_name)
    cmd = ['gdal_calc.py', '-A', resample_tile, '--outfile={}'.format(masked_tile_30), '--calc=A>30', '--NoDataValue=0', '--co', 'COMPRESS=LZW']
    subprocess.check_call(cmd)

    # polygonize tile
    polygonize_cmd = ['./test.sh', '-m', 'parallel', masked_tile_30]
    subprocess.check_call(polygonize_cmd)

    # merge the tile
    combine_cmd = ['./combine.sh', '-t', tile_name]
    subprocess.check_call(combine_cmd)

    # check if there is anything in the file
    driver = ogr.GetDriverByName('ESRI Shapefile')
    datasource = driver.Open('{}.shp'.format(tile_name), 0)
    if datasource is None:
        pass
    else:
        layer = datasource.GetLayer()
        featurecount = layer.GetFeatureCount()
        if featurecount > 0:

            # zip the tile
            os.remove(extent_local)
            merge_shape_list = glob.glob('{}.*'.format(tile_name))
            zipped_tile = '{}.zip'.format(tile_name)
            zip_cmd = ['zip', zipped_tile] +  merge_shape_list
            subprocess.check_call(zip_cmd)

            # upload to s3
            upload_cmd = ['aws', 's3', 'cp', zipped_tile, 's3://gfw2-data/forest_cover/2000_treecover_30_polygons/']
            subprocess.check_call(upload_cmd)

            # clean directory
            files_to_remove = [resample_tile, extent_local, masked_tile_30, zipped_tile] + merge_shape_list
            for file in files_to_remove:
                try:
                    os.remove(file)
                except OSError:
                    pass

        else:
            pass
