FROM python:3.8-alpine

RUN adduser -D flask

WORKDIR /home/flask/flask_quickstart

COPY requirements.txt requirements.txt
RUN python -m venv env
RUN env/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY wsgi.py config.py .env boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_ENV development

RUN chown -R flask:flask ./
USER flask

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
