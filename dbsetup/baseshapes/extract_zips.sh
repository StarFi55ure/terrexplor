#!/bin/bash

#unzip land polygons
unzip land-polygons-split-3857.zip
unzip simplified-land-polygons-complete-3857.zip

# unzip populated places
mkdir ne_10m_populated_places
cd ne_10m_populated_places

unzip ../ne_10m_populated_places_simple.zip

cd ..

# unzip populated places
mkdir ne_10m_admin_0_countries
cd ne_10m_admin_0_countries

unzip ../ne_10m_admin_0_countries.zip

cd ..

