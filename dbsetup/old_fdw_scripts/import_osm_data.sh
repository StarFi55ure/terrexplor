#!/bin/bash

osm2pgsql -C 16000 -d terrexplor -H localhost -U terrexplor --flat-nodes flatnodes -W -k -G --slim --unlogged --number-processes 8 $1


