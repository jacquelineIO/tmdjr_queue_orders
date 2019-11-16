#!/bin/bash
# Docker container start-up script
ls -l venv/bin/activate
source venv/bin/activate
echo "current dir"
pwd

echo "venv exist"
ls -l venv/bin/activate

echo "which flask"
which flask

echo "find flask"
find . -name "flask"

echo "module"
ls /home/tmdjr_queue_orders/

while true; do
    flask db init
    flask db migrate
    flask db upgrade
    if [ "$?" == "0" ]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    sleep 5
done
#flask translate compile
exec gunicorn -b :5000 --access-logfile - --error-logfile - wsgi:app
##exec gunicorn -b :5000 --access-logfile - --error-logfile - tmdjr_queue_orders:app
