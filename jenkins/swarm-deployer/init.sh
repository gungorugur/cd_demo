#!/bin/bash

JENKINS_URL=$1
JENKINS_USER=$2
JENKINS_PASS=$3
JENKINS_LABELS=$4

sudo chmod 777 /var/run/docker.sock

echo Connecting to $JENKINS_URL

java -jar client.jar -master $JENKINS_URL -username $JENKINS_USER -password $JENKINS_PASS -labels $JENKINS_LABELS -executors 2 -mode exclusive