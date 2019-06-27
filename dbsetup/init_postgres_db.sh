#!/bin/bash

psql -d gis -U gis -h localhost <<  EOF
create extension postgis;
create extension hstore;
alter table geometry_columns owner to gis;
alter table spatial_ref_sys owner to gis;

\q
EOF
