#!/bin/bash
echo "here"
DATA=`find . -name '*.shp'`
ogr2ogr -a_srs EPSG:4326 merge.shp
for i in $DATA
do
SHP=${i:9:100}
FINAL="${SHP/.shp/}"
echo $FINAL
echo $i
ogr2ogr -append -update merge.shp $i -f "Esri Shapefile"
done
