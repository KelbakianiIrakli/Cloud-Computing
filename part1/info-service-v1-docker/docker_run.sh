#!/bin/env bash

./build.sh

DB_HOST=127.0.0.1
DB_PORT=3306
DB_DBNAME=watches
DB_USER=watches
DB_PASS=watches

docker run -d --network=host \
	-e DB_HOST=$DB_HOST \
	-e DB_PORT=$DB_PORT \
	-e DB_DBNAME=$DB_DBNAME \
	-e DB_USER=$DB_USER \
	-e DB_PASS=$DB_PASS \
	info-service-v1
