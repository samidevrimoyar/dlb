#!/bin/bash
CONTAINER_ID="15a58bb4a845"
PID=$(docker inspect --format '{{.State.Pid}}' $CONTAINER_ID)
echo "Killing PID $PID"
echo 'Devr2938' | sudo -S kill -9 $PID
echo 'Devr2938' | sudo -S docker rm -f $CONTAINER_ID
echo 'Devr2938' | sudo -S docker compose -f /home/devrim/dlb/docker-compose.yml up -d --build
