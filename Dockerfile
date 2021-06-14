FROM python:3.9-alpine

RUN apk update && apk upgrade

RUN apk add py3-pip python3-dev gcc linux-headers musl-dev bash

RUN pip3 install pipenv

COPY ./Pipfile ./Pipfile

COPY ./Pipfile.lock /ddict/Pipfile.lock

RUN python -m pipenv install --deploy --ignore-pipfile

WORKDIR /ddict

COPY ./app ./app

COPY ./wsgi.py .

EXPOSE 8000

CMD [ "pipenv","run","start" ]
