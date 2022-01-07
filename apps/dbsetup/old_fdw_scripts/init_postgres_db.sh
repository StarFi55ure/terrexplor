#!/bin/bash

#set -x

# Notes:
#
# This script expects a terrexplor role to already exist. This role will own all the databases.
# terrexplor user must also be a superuser.
#

# some pre script setup
. globals


# create main db
function create_main_db {
    $POSTPSQL -c "create database terrexplor owner terrexplor;"
    for i in postgis hstore pgcrypto '"uuid-ossp"' postgres_fdw; do
        $POSTPSQL -d terrexplor -c "create extension if not exists ${i};"
    done

    cat sql/setup_main_database.sql | psql -d terrexplor -U terrexplor -h localhost
}


# create osm databases
function create_osm_databases {
    $POSTPSQL -c "create database osm_derived owner terrexplor"
    for i in $(cat country_partition_databases.dat | awk '{print $1}'); do 
        $POSTPSQL -c "create database ${i} owner terrexplor;"
        $POSTPSQL -d $i -c "create extension if not exists postgis;"
        $POSTPSQL -d $i -c "create extension if not exists hstore;"
    done
}

# fill osm databases with data

function populate_osm_databases {
    echo "populate database"

    while read line; do
        if [ -z "$line" ]; then
            continue
        fi
        dbname=$(echo "$line" | awk '{print $1}')
        url=$(echo "$line" | awk '{print $2}')
        pbffile=$(basename "$url")

        if [ -e osm2pgsql_done_list.txt ] && cat osm2pgsql_done_list.txt | grep "$dbname"; then
            echo ">>> database already provisioned"
            continue
        fi
        osm2pgsql -C 16000 -d $dbname -H localhost -U terrexplor -k -G --slim --unlogged --number-processes 4 osm_pbf_files/$pbffile 2>&1
        echo "$dbname" >> osm2pgsql_done_list.txt
    done < country_partition_databases.dat
}

function clear_osm_fdw {
    echo 'clearing fdw'

}

function create_osm_fdw {
    echo 'create fdw'
    ./generate_fdw_sql.py
}


# execution sequence

create_main_db
create_osm_databases

populate_osm_databases

clear_osm_fdw
create_osm_fdw



