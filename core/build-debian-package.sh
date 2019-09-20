#!/bin/bash

ROOT_DIR=$PWD
SOURCE_PKG_FILE="terrexplor-core-0.0.1.tar.gz"
SOURCE_PKG="$PWD/target/$SOURCE_PKG_FILE"
BUILD_DIR=packaging-build

if [ ! -d $BUILD_DIR ]; then 
    mkdir -p $BUILD_DIR
fi

cp $SOURCE_PKG $BUILD_DIR/

cd $BUILD_DIR
tar xf $SOURCE_PKG_FILE
cd "terrexplor-core_0.0.1"

pdebuild

# move build products into build dir

cp /var/cache/pbuilder/result/terrexplor-core* $ROOT_DIR/$BUILD_DIR/
cd $ROOT_DIR

exit 0

