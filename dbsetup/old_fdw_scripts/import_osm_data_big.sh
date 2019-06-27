#!/bin/bash

osm2pgsql -C 16000 -d terrexplor_import -H localhost -U terrexplor --flat-nodes flatnodes -W -k -G --slim --unlogged --number-processes 4 $1


