#!/bin/env bash

# Webservice must be available on http://localhost:1080/

DB_HOST=db # Use 'db' name for the docker-compose image!
DB_PORT=3306
DB_DBNAME=watches
DB_USER=watches
DB_PASS=watches

export DB_HOST DB_PORT DB_DBNAME DB_USER DB_PASS

docker-compose -f stack.yml up
