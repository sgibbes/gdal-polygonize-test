#!/bin/bash
echo "here"
set -eu

function usage() {
    echo -n "$0

USAGE: $0 [tileid]

OPTIONS:
-t
    tile name.
"
}

function get_opts(){
    while getopts ":t:" opt; do
        case $opt in
            t) TILEID=$OPTARG;;
        esac
    done
    ARGC=$(($#-(OPTIND-1)))
    #shift $((OPTIND-1))

    if [[ $ARGC -eq 1 ]]; then
        INPUT=${1:-0}
    fi

}

function main() {

    get_opts $@

    echo ${TILEID}.shp
    DATA=`find output/ -name '*.shp'`
    for i in $DATA
    do
    echo $i
    ogr2ogr -append -update ${TILEID}.shp $i -f "Esri Shapefile"
    done
}

main $@
