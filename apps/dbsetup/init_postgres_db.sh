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
    cat sql/setup_main_database.sql | psql -d terrexplor -U terrexplor -h localhost
}


# fill osm databases with data

function populate_database {
    echo "populate database"

    if [ -e osm2pgsql_done_list.txt ] && cat osm2pgsql_done_list.txt | grep "terrexplor"; then
        echo ">>> database already provisioned"
        return
    fi

    osm2pgsql -C 16000 -W -d terrexplor -H localhost -U terrexplor -k -G --slim --number-processes 4  \
      osm_pbf_files/$1 2>&1

    if [ $? = 0 ]; then
      echo "Success"
      echo "terrexplor" >> osm2pgsql_done_list.txt
    fi
}

# execution sequence

create_main_db
populate_database south-africa-and-lesotho-latest.osm.pbf



