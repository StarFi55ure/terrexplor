#!/bin/bash

shp2pgsql -d -D -s EPSG:3857 -i -I simplified-land-polygons-complete-3857/simplified_land_polygons.shp \
  osm.baseshapes_simplified_land_polygons > simplified-land-polygons-complete-3857.sql


shp2pgsql -d -D -s EPSG:3857 -i -I land-polygons-split-3857/land_polygons.shp \
  osm.baseshapes_land_polygons_split > land-polygons-split-3857.sql


shp2pgsql -d -D -s EPSG:4326 -i -I ne_10m_populated_places/ne_10m_populated_places_simple.shp \
  osm.baseshapes_ne_10m_pop_places > ne_10m_pop_places.sql


shp2pgsql -d -D -s EPSG:4326 -i -I ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp \
  osm.baseshapes_ne_10m_admin_0_countries > ne_10m_admin_0_countries.sql

