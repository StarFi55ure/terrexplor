#!/bin/bash

osm2pgsql -C 16000 -d gis -H localhost -U gis -W -k -G --slim --unlogged --number-processes 2 $1

