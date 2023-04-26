#!/bin/bash

. globals


for i in $(cat country_partition_databases.dat); do
    $POSTPSQL -c "drop database ${i};"
done

$POSTPSQL -c "drop database osm_derived;"
