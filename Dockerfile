#FROM python:3.7-buster
FROM python:3.7-slim-buster
##FROM python:3.7-alpine

#RUN adduser -D tmdjr_queue_orders
RUN useradd -ms /bin/bash tmdjr_queue_orders

WORKDIR /home/tmdjr_queue_orders

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY app/.flaskenv app/.flaskenv
COPY app/data/* app/data/
#COPY migrations migrations
COPY README.md config.py boot.sh ./
COPY wsgi.py wsgi.py
RUN chmod +x boot.sh

##ENV FLASK_APP queue_orders.py
# The ENV command sets an environment variable inside the container. I need to set FLASK_APP, which is required to use the flask command.

RUN chown -R tmdjr_queue_orders:tmdjr_queue_orders ./
USER tmdjr_queue_orders

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
