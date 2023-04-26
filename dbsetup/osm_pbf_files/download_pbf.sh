#!/bin/bash


for url in $(cat pbf_urls.dat); do
    wget -c $url
done
