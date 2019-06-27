"use strict";

var cluster = require('cluster');
var numCPU = require('os').cpus().length;
var maxCPU = 4;

var tilestrata = require('tilestrata');
var disk = require('tilestrata-disk');
var mapnik = require('tilestrata-mapnik');
var nodeMapnik = require('mapnik');
var blend = require('tilestrata-blend');
var express = require('express');

nodeMapnik.Logger.setSeverity(nodeMapnik.Logger.NONE);

var buildMapnikProjectFiles = function () {
    //console.log('TODO: checking if need to rebuild project.xml');
};

buildMapnikProjectFiles();

function setupTileServer () {
    var strata = tilestrata();
    strata.layer('combined')
        .route('tile.png')
        .use(disk.cache({
            dir: './cache/maintheme-osmbright'
        }))
        .use(mapnik({
            pathname: 'themes/maintheme-osmbright/project.xml',
            tileSize: 256
        }));

    strata.layer('infrastructure-hillshade')
        .route('tile.png')
        .use(disk.cache({
            dir: './cache/infrastructure-hillshade'
        }))
        .use(blend([
            ['infrastructure', 'tile.png'],
            ['hillshade', 'tile.png', {
                opacity: 0.5
            }]
        ], {
            matte: 'ffffff'
        }));

    strata.layer('infrastructure')
        .route('tile.png')
        .use(disk.cache({
            dir: './cache/infrastructure'
        }))
        .use(mapnik({
            pathname: 'themes/infrastructure/project.xml',
            tileSize: 256
        }));

    strata.layer('hillshade')
        .route('tile.png')
        .use(disk.cache({
            dir: './cache/hillshade-built'
        }))
        .use(mapnik({
            pathname: 'themes/hillshade-built-layer/project.xml',
            tileSize: 256
        }));

    var app = express();

    app.use(function (req, res, next) {
        res.header("Access-Control-Allow-Origin", "*");
        res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        next();
    });

    app.use(tilestrata.middleware({
        server: strata,
        prefix: '/tiles'
    }));

    app.listen(6789, function () {
        console.log('Starting server on port 6789');
    });
}


function eachWorker(callback) {
    for (const id in cluster.workers) {
        callback(cluster.workers[id]);
    }
}

var numStartedWorkers = 0;

if (cluster.isMaster) {
    console.log(`Master Tile Server Process ${process.pid}`);

    for (let i=0; i<Math.min(numCPU, maxCPU); i++) {
        cluster.fork();
        numStartedWorkers++;
    }

    process.on('SIGTERM', () => {
        console.log('Killing workers');
        eachWorker((worker) => {
            worker.kill();
        });
    });

    cluster.on('exit', (worker, code, signal) => {
        numStartedWorkers--;
        console.log(`Worker ${worker.process.pid} exited`);

        if (numStartedWorkers < 1) {
            console.log('Exiting');
        }
    });
} else {
    console.log(`In Child Tile Process ${process.pid}`);
    setupTileServer();
}















