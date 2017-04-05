#!/bin/bash

DATA=`find . -name 'output/*.shp'`
ogr2ogr -a_srs EPSG:4326 merge.shp
for i in $DATA
do
SHP=${i:2:100}
FINAL="${SHP/.shp/}"
echo $FINAL
echo $i
ogr2ogr -append -update merge.shp $i -f "Esri Shapefile" -dialect sqlite -sql "SELECT * FROM $FINAL WHERE DN = 1"
done