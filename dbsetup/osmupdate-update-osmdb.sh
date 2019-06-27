#!/bin/bash

UPDATE_WORKDIR=/home/deployment/gisplayarea/dbsetup


LAST_UPDATE_FILE=planet-last-update.osc
LATEST_UPDATE_FILE=planet-`date +%Y-%m-%d_%H:%M:%S`.osc

old_dir=$PWD
cd $UPDATE_WORKDIR

if [ ! -e $LAST_UPDATE_FILE ]; then
    cp planet-latest.osm.pbf planet-latest.osm.pbf.orig
    LAST_UPDATE_FILE=planet-latest.osm.pbf
fi


/usr/bin/osmupdate -v $LAST_UPDATE_FILE $LATEST_UPDATE_FILE

/usr/bin/osm2pgsql --slim --append -C 6000 --number-processes 2 -d gis -U gis -H localhost $LATEST_UPDATE_FILE

# rotate files
rm -f $LAST_UPDATE_FILE
cp $LATEST_UPDATE_FILE $LAST_UPDATE_FILE


