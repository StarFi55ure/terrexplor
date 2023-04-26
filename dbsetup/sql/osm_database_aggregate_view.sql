
create or replace view planet_osm_line as
    {% for db in databases %}
        select * from {{db}}.planet_osm_line {% if not loop.last %} union all {% endif %} 
    {% endfor %}
    ;

create or replace view planet_osm_nodes as
    {% for db in databases %}
        select * from {{db}}.planet_osm_nodes {% if not loop.last %} union all {% endif %} 
    {% endfor %}
    ;

create or replace view planet_osm_point as
    {% for db in databases %}
        select * from {{db}}.planet_osm_point {% if not loop.last %} union all {% endif %} 
    {% endfor %}
    ;

create or replace view planet_osm_polygon as
    {% for db in databases %}
        select * from {{db}}.planet_osm_polygon {% if not loop.last %} union all {% endif %} 
    {% endfor %}
    ;

create or replace view planet_osm_rels as
    {% for db in databases %}
        select * from {{db}}.planet_osm_rels {% if not loop.last %} union all {% endif %} 
    {% endfor %}
    ;

create or replace view planet_osm_roads as
    {% for db in databases %}
        select * from {{db}}.planet_osm_roads {% if not loop.last %} union all {% endif %} 
    {% endfor %}
    ;

create or replace view planet_osm_ways as
    {% for db in databases %}
        select * from {{db}}.planet_osm_ways {% if not loop.last %} union all {% endif %} 
    {% endfor %}
    ;

