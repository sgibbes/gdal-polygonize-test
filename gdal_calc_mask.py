import subprocess

def mask_tile(tile_id, input_tif):
    # mask the tcd tile to only have values greater than 30
    
	masked_tile_30 = '--outfile={}.tif'.format(tile_id)

	cmd = [r'C:\Program Files\GDAL\gdal_calc.py', '-A', input_tif, outfile, '--calc="A>30"', '--NoDataValue=0', '-co', 'COMPRESS=LZW']

	subprocess.check_call(cmd)

	return masked_tile_30
