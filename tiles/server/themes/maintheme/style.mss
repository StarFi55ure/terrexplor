Map {
    background-color: #93c4ff;
}

@land-base-fill: #f6f4f4;


#land-low[zoom>=0][zoom<@detail-switch-level],
#land-high[zoom>=@detail-switch-level] {
    /*::outline {
        line-color:#979800;
        line-width:0.5;
        line-join: round;
    }*/
    polygon-opacity:1;
    /* polygon-fill:#f0f0f0; */
    polygon-fill: @land-base-fill;

}

#land-high-tint-band::tint-band [zoom>=10] {
    line-color: #b0b0b0;
    line-width: 0;

    polygon-fill: #5d86a1;

    image-filters: agg-stack-blur(10, 10);
    /*image-filters-inflate: true;*/
}


#countries[zoom<@detail-switch-level] {
    line-color: darken(@land-base-fill, 20%);
    line-width:2;
    polygon-opacity: 1;
    polygon-fill: @land-base-fill;
}

