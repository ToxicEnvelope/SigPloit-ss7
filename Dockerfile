FROM alpine:3.7

RUN apk update && apk upgrade && apk add --no-cache bash
RUN apk add --no-cache --virtual=build-dependencies unzip
RUN apk add --no-cache curl && apk add --no-cache openjdk8-jre
RUN apk add --no-cache python3 && python3 -m ensurepip && pip3 install --upgrade pip setuptools

ADD ss7 /app
ADD . /app
ADD venv /app
