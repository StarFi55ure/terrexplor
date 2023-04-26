
create extension if not exists postgis;
create extension if not exists hstore;
create extension if not exists pgcrypto;
create extension if not exists "uuid-ossp";
create extension if not exists ltree;

alter table geometry_columns owner to terrexplor;
alter table spatial_ref_sys owner to terrexplor;

create schema if not exists osm;
