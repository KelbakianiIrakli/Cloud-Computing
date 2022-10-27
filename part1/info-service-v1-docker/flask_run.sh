#!/bin/env bash

DB_HOST=127.0.0.1
DB_PORT=3306
DB_DBNAME=watches
DB_USER=watches
DB_PASS=watches
export DB_HOST DB_PORT DB_DBNAME DB_USER DB_PASS

# By default app.py on port 5000
flask --debug run
