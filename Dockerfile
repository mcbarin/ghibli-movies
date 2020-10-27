FROM python:3.6.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc linux-headers postgresql-dev
RUN pip install --upgrade pip -r /requirements.txt
RUN apk del .tmp-build-deps
RUN apk --update add \
    build-base

RUN mkdir /app
WORKDIR /app
COPY ./ /app
