#!/bin/bash

NEXUS_USER=$1
NEXUS_PASS=$2

echo Downloading nexus docker image

docker pull sonatype/nexus3:3.14.0

sleep 15

echo Deploying nexus service

docker stack deploy -c docker-compose-stack.yml nexus

echo Creating private docker registry

python3 create-docker-registry.py http://127.0.0.1:8081 $NEXUS_USER $NEXUS_PASS