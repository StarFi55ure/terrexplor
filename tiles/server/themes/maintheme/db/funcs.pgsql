-- Function to get OSM data for mapnik


------------------------------------------
-- ROADS
------------------------------------------


create or replace view thm_maintheme__roads_high as 

select way
    ,highway as type
from planet_osm_line
where highway is not null
    and (tunnel is null or tunnel = 'no')
    and (bridge is null or bridge = 'no')

;


