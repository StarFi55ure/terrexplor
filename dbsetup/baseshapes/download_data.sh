#!/bin/bash

CWD=$(dirname `readlink -f $0`)
echo "Working from $CWD"

cd $CWD
#wget -c http://data.openstreetmapdata.com/simplified-land-polygons-complete-3857.zip
wget -c https://osmdata.openstreetmap.de/download/simplified-land-polygons-complete-3857.zip
#wget -c http://data.openstreetmapdata.com/land-polygons-split-3857.zip
wget -c https://osmdata.openstreetmap.de/download/land-polygons-split-3857.zip
wget -c https://www.naturalearthdata.com/http\//www.naturalearthdata.com/download/10m/cultural/ne_10m_populated_places_simple.zip
wget -c https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries.zip

