FROM python:3.8.3-slim-buster

WORKDIR '/nnst'
COPY . '/nnst'

RUN pip install pipenv==2018.11.26 && pipenv install --ignore-pipfile --system

CMD nnst serve
