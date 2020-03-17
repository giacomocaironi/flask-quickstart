FROM python:3.8-alpine

RUN adduser -D flask

WORKDIR /home/flask/flask_quickstart

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install psycopg2-binary

COPY app app
COPY migrations migrations
COPY wsgi.py config.py boot.sh ./
RUN chmod +x boot.sh

RUN chown -R flask:flask ./
USER flask

ENTRYPOINT ["./boot.sh"]
