var glob = require('glob');
var xmlbuilder = require('xmlbuilder');

var files = glob.sync('output/hillshade/**/*.tif');

var xml_root = xmlbuilder.create({
                    Map: {
                        '@srs': '+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over',
                        '@background-color': '#ffffff'
                    }
                },
                {
                    version: '1.0',
                    encoding: 'UTF-8'
                });

var parameters = xml_root.ele({
    Parameters: ''
});

var params = {
    bounds: '-180,-85.05112877980659,180,85.05112877980659',
    center: '0,0,2',
    format: 'png8',
    minzoom: 0,
    maxzoom: 22,
    scale: 1,
    name: "GISPlayarea Hillshade"
};

for (var k in params) {
    if(params.hasOwnProperty(k)) {
        var v = params[k];
        parameters.ele({
            Parameter: {
                '@name': k,
                '#text': v
            }
        })
    }
}

var Style = xml_root.ele({
    Style: {
        '@name': 'raster',
        Rule: {
            RasterSymbolizer: {
                '@opacity': 1
            }
        }
    }
})

files.forEach(function(file) {
    var Layer = xml_root.ele({
        Layer: {
            '@name': file,
            '@status': 'on',
            StyleName: 'raster',
            Datasource: {
                Parameter: [
                    {
                        '@name': 'type',
                        '#cdata': 'gdal'
                    },
                    {
                        '@name': 'file',
                        '#text': file
                    }
                ]
            }
        }
    });
});

var dtd = xml_root.dtd();
var final_xml = xml_root.end({
    pretty: true,
    index: '  '
});
console.log(final_xml);
