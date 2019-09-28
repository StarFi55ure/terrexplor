#!/bin/bash

psql -d terrexplor -U terrexplor -h localhost <<  EOF
create extension postgis;
create extension hstore;
alter table geometry_columns owner to terrexplor;
alter table spatial_ref_sys owner to terrexplor;

\q
EOF
