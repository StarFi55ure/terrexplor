import {Component, OnInit, ViewEncapsulation} from '@angular/core';

import {Map as olMap, View} from "ol";
import TileLayer from 'ol/layer/Tile';
import XYZ from 'ol/source/XYZ';
import {transform} from "ol/proj";
import {defaults} from "ol/control";
import {ApiService} from "../../services/api.service";
import {UserService} from "../../services/user.service";

@Component({
    selector: 'app-home',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.scss'],
    encapsulation: ViewEncapsulation.None
})
export class HomeComponent implements OnInit {

    private MainMap: any;

    constructor(
        private userService: UserService
    ) {
    }

    ngOnInit(): void {
        // var tileUrl = config['tileserver.url'];
        // var tileTheme = config['tileserver.theme'];
        // var defaultLonLat = config['tileserver.defaultLonLat'];
        // var defaultMaxZoom = config['tileserver.defaultMaxZoom'];
        // var defaultZoom = config['tileserver.defaultZoom'];

        //var OSMTileServer = tileUrl + '/' + tileTheme + '/{z}/{x}/{y}/tile.png'
        // var OSMTileServer = "https://tile.openstreetmap.org/{z}/{x}/{y}.png";

        //var OSMTileServer =
        // "http://tiles-dev-{a-d}.privatenet.local/tiles/tiles/1.0.0/maintheme/geodetic/{z}/{x}/{y}.png";
        // var OSMTileServer = "https://tile.openstreetmap.org/{z}/{x}/{y}.png";
        // var OSMTileServer = "http://localhost:6789/tiles/1.0.0/maintheme/{z}/{x}/{y}.png";


        var OSMTileServer = "http://localhost:6789/tiles/tiles/1.0.0/maintheme/geodetic/{z}/{x}/{y}.png";

        // setup base layer
        var tileLayer = new TileLayer({
            // preload: Infinity,
            source: new XYZ({
                url: OSMTileServer
            })
        });

        // var fill = new ol.style.Fill({
        //     color: 'rgba(0, 0, 200, 0.2)'
        // });
        //
        // var stroke = new ol.style.Stroke({
        //     color: 'rgba(0, 0, 0, 0.4)'
        // });
        //
        // var vectorStyleRange = new ol.style.Style({
        //     fill: fill,
        //     stroke: stroke,
        //     image: new ol.style.Circle({
        //         radius: 50,
        //         fill: fill,
        //         stroke: stroke
        //     })
        // });
        //
        // var vectorStyleIcon = new ol.style.Style({
        //     fill: fill,
        //     stroke: stroke,
        //     image: new ol.style.Icon({
        //         src: '/images/policeman-48x48.png'
        //     })
        // });
        //
        // var vectorLoader = function (extent, resolution, projection) {
        //     //console.log('extent: ' + extent.join(','));
        //     // api.getDrainageStations({
        //     //     bbox: extent.join(',')
        //     // }).then(function (res) {
        //     //     var freader = new ol.format.GeoJSON();
        //     //     res.geojson = JSON.parse(res.geojson);
        //     //     var features = freader.readFeatures(res.geojson);
        //     //     for (var i = 0; i < features.length; i++) {
        //     //         features[i].setId(features[i].get('id'));
        //     //         //TODO: must convert on server side
        //     //         features[i].getGeometry().transform("EPSG:4326", "EPSG:3857");
        //     //     }
        //     //     vectorSource.addFeatures(features);
        //     // });
        // };

        // var styleFunction = function (feature, resolution) {
        //
        //     var range_radius = 2 * 1000;
        //
        //     var view = MainMap.getView();
        //     var projection = view.getProjection();
        //     var viewResolution = view.getResolution();
        //     var center = view.getCenter();
        //
        //     var geom = feature.getGeometry();
        //     var extent = geom.getExtent();
        //     var X = (extent[0] + (extent[2] - extent[0])) / 2;
        //     var Y = (extent[1] + (extent[3] - extent[1])) / 2;
        //
        //     var featurePoint = new ol.geom.Point([X, Y]);
        //
        //     // TODO: might need to check what the difference is with a toggle switch
        //     // calculate adjusted resolution for point
        //     var resolutionAtPoint = ol.proj.getPointResolution(projection, viewResolution, featurePoint.getCoordinates());
        //
        //     var radius_pixels = range_radius / resolutionAtPoint
        //
        //     var vsr = new ol.style.Style({
        //         fill: fill,
        //         stroke: stroke,
        //         image: new ol.style.Circle({
        //             radius: radius_pixels,
        //             fill: fill,
        //             stroke: stroke
        //         })
        //     });
        //
        //     return [vsr, vectorStyleIcon];
        // };
        //
        // var vectorSource = new ol.source.Vector({
        //     format: new ol.format.GeoJSON(),
        //     loader: vectorLoader,
        //     strategy:
        //     ol.loadingstrategy.bbox,
        //     //     ol.loadingstrategy.tile(ol.tilegrid.createXYZ({
        //     //         minZoom: 11,
        //     //         maxZoom: 19
        //     //     }))
        // });

        // vectorSource.on('addfeature', function () {
        // });
        //
        // var clusterSource = new ol.source.Cluster({
        //     distance: 50,
        //     source: vectorSource
        // });
        //
        // var vectorLayer = new ol.layer.Vector({
        //     source: vectorSource,
        //     updateWhileAnimating: false,
        //     updateWhileInteracting: false,
        //     minResolution: 0,
        //     maxResolution: 100,
        //
        //     style: styleFunction
        // });


        // setup main map widget
        this.MainMap = new olMap({
            target: 'mainmap',
            loadTilesWhileAnimating: false,
            loadTilesWhileInteracting: false,
            layers: [
                tileLayer
                //vectorLayer
            ],
            controls: defaults({
                attributionOptions: {
                    collapsible: true
                }
            }),
            view: new View({
                maxZoom: 18,
                center: transform([18.417, -33.928], 'EPSG:4326', 'EPSG:3857'),
                zoom: 11,
                projection: 'EPSG:3857'
            })
        });
    }

}
