FROM python:3.9-alpine

RUN apk update && apk upgrade

RUN apk add py3-pip python3-dev gcc linux-headers musl-dev bash libffi-dev openssl-dev

RUN python -m pip install --upgrade pip

RUN pip3 install pipenv

COPY ./Pipfile ./Pipfile

COPY ./Pipfile.lock /ddict/Pipfile.lock

RUN python -m pipenv install --deploy --ignore-pipfile

WORKDIR /ddict

EXPOSE 8000

CMD [ "pipenv","run","start" ]
