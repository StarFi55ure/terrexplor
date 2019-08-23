
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
                var OSMTileServer = "https://tile.openstreetmap.org/{z}/{x}/{y}.png";
                //var OSMTileServer =
                // "http://localhost:6789/tiles/terrexplor-main/{z}/{x}/{y}/tile.png";

                // setup base layer
                var tileLayer = new ol.layer.Tile({
                    preload: Infinity,
                    source: new ol.source.OSM({
                        attributions: [
                            ol.source.OSM.ATTRIBUTION
                        ],
                        url: OSMTileServer
                    })
                });

                var fill = new ol.style.Fill({
                    color: 'rgba(0, 0, 200, 0.2)'
                });

                var stroke = new ol.style.Stroke({
                    color: 'rgba(0, 0, 0, 0.4)'
                });

                var vectorStyleRange = new ol.style.Style({
                    fill: fill,
                    stroke: stroke,
                    image: new ol.style.Circle({
                        radius: 50,
                        fill: fill,
                        stroke: stroke
                    })
                });

                var vectorStyleIcon = new ol.style.Style({
                    fill: fill,
                    stroke: stroke,
                    image: new ol.style.Icon({
                        src: '/images/policeman-48x48.png'
                    })
                });

                var vectorLoader = function (extent, resolution, projection) {
                    //console.log('extent: ' + extent.join(','));
                    // api.getDrainageStations({
                    //     bbox: extent.join(',')
                    // }).then(function (res) {
                    //     var freader = new ol.format.GeoJSON();
                    //     res.geojson = JSON.parse(res.geojson);
                    //     var features = freader.readFeatures(res.geojson);
                    //     for (var i = 0; i < features.length; i++) {
                    //         features[i].setId(features[i].get('id'));
                    //         //TODO: must convert on server side
                    //         features[i].getGeometry().transform("EPSG:4326", "EPSG:3857");
                    //     }
                    //     vectorSource.addFeatures(features);
                    // });
                };

                var styleFunction = function (feature, resolution) {

                    var range_radius = 2 * 1000;

                    var view = MainMap.getView();
                    var projection = view.getProjection();
                    var viewResolution = view.getResolution();
                    var center = view.getCenter();

                    var geom = feature.getGeometry();
                    var extent = geom.getExtent();
                    var X = (extent[0] + (extent[2] - extent[0])) / 2;
                    var Y = (extent[1] + (extent[3] - extent[1])) / 2;

                    var featurePoint = new ol.geom.Point([X, Y]);

                    // TODO: might need to check what the difference is with a toggle switch
                    // calculate adjusted resolution for point
                    var resolutionAtPoint = ol.proj.getPointResolution(projection, viewResolution, featurePoint.getCoordinates());

                    var radius_pixels = range_radius / resolutionAtPoint

                    var vsr = new ol.style.Style({
                        fill: fill,
                        stroke: stroke,
                        image: new ol.style.Circle({
                            radius: radius_pixels,
                            fill: fill,
                            stroke: stroke
                        })
                    });

                    return [vsr, vectorStyleIcon];
                };

                var vectorSource = new ol.source.Vector({
                    format: new ol.format.GeoJSON(),
                    loader: vectorLoader,
                    strategy:
                    ol.loadingstrategy.bbox,
                    //     ol.loadingstrategy.tile(ol.tilegrid.createXYZ({
                    //         minZoom: 11,
                    //         maxZoom: 19
                    //     }))
                });

                vectorSource.on('addfeature', function () {
                });

                var clusterSource = new ol.source.Cluster({
                    distance: 50,
                    source: vectorSource
                });

                var vectorLayer = new ol.layer.Vector({
                    source: vectorSource,
                    updateWhileAnimating: false,
                    updateWhileInteracting: false,
                    minResolution: 0,
                    maxResolution: 100,

                    style: styleFunction
                });


                // setup main map widget
                MainMap = new ol.Map({
                    target: 'mainmap',
                    loadTilesWhileAnimating: false,
                    loadTilesWhileInteracting: false,
                    layers: [
                        tileLayer,
                        vectorLayer
                    ],
                    controls: ol.control.defaults({
                        attributionOptions: {
                            collapsible: true
                        }
                    }),
                    view: new ol.View({
                        maxZoom: defaultMaxZoom,
                        center: ol.proj.transform(defaultLonLat, 'EPSG:4326', 'EPSG:3857'),
                        zoom: defaultZoom
                    })
                });

            }
        }
    })
});
