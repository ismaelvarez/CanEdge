#!/bin/bash

cd /usr/app/src/canedge-influxdb-writer/dashboard-writer

while [ true ]
do
python main.py
sleep ${CANDEGDE_UPDATE_PERIOD}m
done
