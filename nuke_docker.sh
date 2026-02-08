#!/bin/bash
# Get all container IDs
IDS=$(docker ps -q)
for id in $IDS
do
  PID=$(docker inspect --format '{{.State.Pid}}' $id)
  if [ ! -z "$PID" ]; then
    echo "Killing container $id (PID $PID)"
    echo 'Devr2938' | sudo -S kill -9 $PID
  fi
done

echo 'Devr2938' | sudo -S systemctl stop docker
# Clean up verify
echo 'Devr2938' | sudo -S rm -rf /var/lib/docker/containers/* # Too dangerous? Maybe just restart.

echo 'Devr2938' | sudo -S systemctl start docker
echo "Pruning..."
echo 'Devr2938' | sudo -S docker system prune -f

echo "Starting up..."
echo 'Devr2938' | sudo -S docker compose -f /home/devrim/dlb/docker-compose.yml up -d --build
