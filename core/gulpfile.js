
var gulp        = require('gulp');
var less        = require('gulp-less');
var concat      = require('gulp-concat');
var watch       = require('gulp-watch');
var sourcemaps  = require('gulp-sourcemaps');
var exec        = require('child_process').exec;
var execFile    = require('child_process').execFile;

//=================================================
// Web Assets
//=================================================


gulp.task('css-app', function() {
    "use strict";

    return gulp.src('src/main/resources/static/less/main.less')
        .pipe(less({
            strictMath: true
        }))
        .pipe(concat('app.css'))
        .pipe(gulp.dest('src/main/resources/static/css'))
});

gulp.task('css-vendor', function() {
    "use strict";

    var sources = [
        'node_modules/bootstrap/dist/css/bootstrap.min.css',
        'src/main/resources/static/vendors/ol/ol.css'
    ];

    return gulp.src(sources)
        .pipe(concat('vendor.css'))
        .pipe(gulp.dest('src/main/resources/static/css'));
});

gulp.task('css', gulp.parallel(['css-vendor', 'css-app']));


gulp.task('js-vendor', function () {
    "use strict";

    var sources = [
        'node_modules/jquery/dist/jquery.min.js',
        'node_modules/bootstrap/dist/js/bootstrap.min.js',
        'node_modules/vue/dist/vue.min.js',
        'node_modules/lodash/lodash.min.js',
        'src/main/resources/static/vendors/ol/ol.js'
    ];

    return gulp.src(sources)
    //.pipe(sourcemaps.init())
        .pipe(concat('vendor.js'))
        //.pipe(sourcemaps.write())
        .pipe(gulp.dest('src/main/resources/static/js'));
});

gulp.task('js-app', function () {
    "use strict";

    var sources = [
        'src/main/resources/static/js/services/ServiceRegistry.js',
        'src/main/resources/static/js/services/**/*.js',
        'src/main/resources/static/js/components/**/*.js'
    ];

    return gulp.src(sources)
        .pipe(concat('app.js'))
        .pipe(gulp.dest('src/main/resources/static/js'));
});

gulp.task('js', gulp.parallel(['js-vendor', 'js-app']));

//=================================================
// Main Tasks
//=================================================

gulp.task('watch', function () {
    "use strict";

    gulp.watch('src/main/resources/static/less/**/*.less', gulp.series(['css']));
});

gulp.task('default', gulp.parallel(['css', 'js']));
