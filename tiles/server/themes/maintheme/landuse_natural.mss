@landuse-nature-reserve: #b8d0ae;

/*#landuse_gen0[zoom>=10] {

    [type='nature_reserve'] { polygon-fill: @landuse-nature-reserve; }
}*/

#landuse_natural {

    [type='nature_reserve'],
    [type='conservation'],
    [type='forest'],
    [type='recreation_ground'],
    [boundary='national_park'] {
        polygon-fill: @landuse-nature-reserve;
        polygon-opacity: 0.5;
        /*image-filters: agg-stack-blur(5, 5);*/
    }
  
}
