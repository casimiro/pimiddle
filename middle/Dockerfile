FROM python:3.6-slim

ADD requirements.txt /app/requirements.txt

ENV LANG=en_US.UTF-8

RUN pip install -r /app/requirements.txt

WORKDIR /app
ADD * /app/
