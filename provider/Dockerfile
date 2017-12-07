FROM pypy:3-slim

ENV LANG=en_US.UTF-8

ADD * /app/

RUN pip install -r /app/requirements.txt

WORKDIR /app
