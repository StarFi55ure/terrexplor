
let MainView = null;
let MainMap = null;

$(document).ready(function () {

    MainView = new Vue({
        el: '#page-container',
        data: {
            name: "first name"
        },
        mounted: function () {
            console.log('init');

            this.initializeMap();
        },
        methods: {
            initializeMap: function () {
                let config = ServiceRegistry.getInstance().getService('config');
                //let api = ServiceRegistry.getInstance().getService('api');

                var tileUrl = config['tileserver.url'];
                var tileTheme = config['tileserver.theme'];
                var defaultLonLat = config['tileserver.defaultLonLat'];
                var defaultMaxZoom = config['tileserver.defaultMaxZoom'];
                var defaultZoom = config['tileserver.defaultZoom'];

                //var OSMTileServer = tileUrl + '/' + tileTheme + '/{z}/{x}/{y}/tile.png'
                // var OSMTileServer = "https://tile.openstreetmap.org/{z}/{x}/{y}.png";

                var OSMTileServer = "http://localhost:6789/tiles/tms/1.0.0/maintheme/webmercator/{z}/{x}/{-y}.png";

                // setup base layer
                var tileLayer = new ol.layer.Tile({
                    // preload: Infinity,
                    source: new ol.source.XYZ({
                        attributions: [
                            ol.source.OSM.ATTRIBUTION
                        ],
                        extent: [-20037508.342789244, -20037508.342789244, 20037508.342789244, 20037508.342789244],
                        tileGrid: new ol.tilegrid.TileGrid({
                            extent: [-20037508.342789244, -20037508.342789244, 20037508.342789244, 20037508.342789244],
                            origin: [-20037508.342789244, -20037508.342789244],
                            resolutions: [
                                78271.51696402048,
                            	39135.75848201024,
                            	19567.87924100512,
                            	9783.93962050256,
                            	4891.96981025128,
                            	2445.98490512564,
                            	1222.99245256282,
                            	611.49622628141,
                            	305.748113140705,
                            	152.8740565703525,
                            	76.43702828517625,
                            	38.21851414258813,
                            	19.109257071294063,
                            	9.554628535647032,
                            	4.777314267823516,
                            	2.388657133911758,
                            	1.194328566955879,
                            	0.5971642834779395,
                            	0.29858214173896974
                            ]
                        }),
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
                MainMap = new ol.Map({
                    target: 'mainmap',
                    // maxResolution: 78271.51696402048,
                    // units: 'm',
                    // maxExtent: [-20037508.342789244, -20037508.342789244,
                    //     20037508.342789244, 20037508.342789244],
                    loadTilesWhileAnimating: false,
                    loadTilesWhileInteracting: false,
                    layers: [
                        tileLayer
                        //vectorLayer
                    ],
                    controls: ol.control.defaults({
                        attributionOptions: {
                            collapsible: true
                        }
                    }),
                    view: new ol.View({
                        maxZoom: 18,
                        center: ol.proj.transform([18.417, -33.928], 'EPSG:4326', 'EPSG:3857'),
                        zoom: 4
                        //projection: 'EPSG:3857'
                    })
                });

            }
        }
    })
});
