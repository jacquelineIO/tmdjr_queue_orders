FROM python:3.7-alpine

RUN adduser -D tmdjr

WORKDIR /home/tmdjr

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY app/.flaskenv app/.flaskenv
COPY app/data/* app/data/
COPY migrations migrations
COPY README.md config.py boot.sh ./
RUN chmod +x boot.sh

#ENV FLASK_APP microblog.py
# The ENV command sets an environment variable inside the container. I need to set FLASK_APP, which is required to use the flask command.

RUN chown -R tmdjr:tmdjr ./
USER tmdjr

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
