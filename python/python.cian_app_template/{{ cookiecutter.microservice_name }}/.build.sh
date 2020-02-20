#!/bin/sh

docker build -t "docker-infra.cian.ru/{{ cookiecutter.microservice_name }}:$BRANCH_NAME" .
