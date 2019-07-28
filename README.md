# tmdjr_queue_orders

git clone https://github.com/jacquelineIO/tmdjr_queue_orders.git
cd tmdjr_queue_orders

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt

If you get this message to update pip, then update it:
```
You are using pip version 10.0.1, however version 19.2.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```
pip install --upgrade pip

Initial and migrate the Database
This is currently using SQLite3
flask db init
flask db migrate
flask db upgrade

Get a copy of the data file from Google Drive
Place file data_files.tgz in the directory tmdjr_queue_orders/app/data
cd to data folder
tar xvf data_files.tgz

