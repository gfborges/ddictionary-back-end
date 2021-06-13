FROM python:3.9-alpine

RUN apk update && apk upgrade

RUN apk add py3-pip python3-dev gcc linux-headers musl-dev bash

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "wsgi:app" ]
