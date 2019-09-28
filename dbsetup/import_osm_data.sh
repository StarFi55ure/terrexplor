#!/bin/bash

osm2pgsql -C 16000 -d terrexplor -H localhost -U terrexplor -W -k -G --slim --unlogged --number-processes 2 $1

