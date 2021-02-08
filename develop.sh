#!/usr/bin/env bash
NAME="${APP_NAME:-flask0}"
docker build -t $NAME .
docker run -p "8080:8080" -v $PWD/app:/app --env-file $PWD/.dev.env $NAME flask run
