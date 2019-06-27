
@motorway_fill: #FFEA78;
@motorway_case: darken(@motorway_fill, 30%);

@trunk_fill: @primary_fill;
@trunk_case: @primary_case;

@primary_fill: #FDFF93;
@primary_case: darken(@primary_fill, 40%);

@secondary_fill: rgb(255, 255, 255);
@secondary_case: darken(@secondary_fill, 60%);

@tertiary_fill: rgb(255, 255, 255);
@tertiary_case: darken(@tertiary_fill, 40%);

/* Line and Polygon style */


/* Label Styles */

@label-halo-fill: #63944f;
@label-halo-radius: 3px;
@label-text-fill: #f7ff49;


#roads_low {

    ::primary {
        [type='primary'] {
            ::case {
                [zoom>=6] {
                    line-width: 1.5;
                    line-color: lighten(@primary_case, 5%);
                }
                [zoom>=10] {
                    line-width: 3;
                    line-color: @primary_case;
                }
            }

            ::road {
                [zoom>=6] {
                    line-width: 1;
                    line-color: darken(@primary_fill, 30%);
                }

                [zoom>=10] {
                    line-width: 2;
                    line-color: @primary_fill;
                }

            }
        }
    }

    ::trunk {
        [type='trunk'] {
            ::case {
                [zoom>=6] {
                    line-width: 1;
                    line-color: @trunk_case;
                }

                [zoom>=10] {
                    line-width: 5;
                    line-color: @trunk_case;
                }
            }

            ::road {
                [zoom>=6] {
                    line-width: 1;
                    line-color: darken(@trunk_fill, 30%);
                }

                [zoom>=10] {
                    line-width: 3.5;
                    line-color: lighten(@trunk_fill, 10%);
                }
            }
        }
    }

    ::motorway {
        [type='motorway'] {
            ::case {
                [zoom>=1] {
                    line-width: 3;
                    line-color: @motorway_case;
                }
            }

            ::road {
                [zoom>=1] {
                    line-width: 2;
                    line-color: @motorway_fill;
                }


            }
        }
    }

}

#roads_low_label {
    [type='motorway'],
    [type='trunk'] {
        text-name: "[ref]";
        text-face-name: 'DejaVu Sans Book';
        text-fill: @label-text-fill;
        text-min-distance: 100px;
        text-halo-fill: @label-halo-fill;
        text-halo-radius: @label-halo-radius;
        text-size: 10px;
        text-avoid-edges: true;
    }
}

