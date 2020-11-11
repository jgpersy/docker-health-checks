FROM python:3.8-alpine

#Don't buffer python outputs, simply print
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev curl

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /apifizzbuzz
COPY ./app /apifizzbuzz
WORKDIR /apifizzbuzz/apifizzbuzz


RUN adduser -D user
USER user
