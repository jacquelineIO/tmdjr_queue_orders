# tmdjr_queue_orders

## Requirements for install
* Python3
* pip or pip3

## Get copy application
```
git clone https://github.com/jacquelineIO/tmdjr_queue_orders.git
```

## Setup virtual env and install requirements
```
cd tmdjr_queue_orders
```
### Virtual env setup
```
python3 -m venv env
source env/bin/activate
```
### Install requirements to run application
pip install -r requirements.txt

### Misc warning to upgrade pip
If you get this message to update pip, then update it:
```
You are using pip version 10.0.1, however version 19.2.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```
```
pip install --upgrade pip
```
## Setup database
Initial and migrate the Database
This is currently using SQLite3
```
flask db init
flask db migrate
flask db upgrade
```

### Get copy of data dumps to run application in sandbox
Get a copy of the data archive from [Google Drive](https://drive.google.com/drive/u/1/folders/1nAblU72qlTKgcTMgJ-00r5Zy8aVf8Ffc)
Place file `data_files.tgz` in the directory tmdjr_queue_orders/app/data
```
cd tmdjr_queue_orders/app/data
tar xvf data_files.tgz
```

## Create .flaskenv file 
In the directory `thatsmydogjr/queue_orders/app` create a file named `.flaskenv`
put in it the contents.
```
FLASK_APP=queue_orders.py
```

## Run the application
From the `app` folder run the `flask run` command
If you aren't already in the directory, change to the `app` dir
```
cd tmdjr_queue_orders/app/
```
### Run Flask application
```
flask run
```
When the application is running at the console for a message similiar to
```
Running on http://127.0.0.1:5000/
```
When you this message use this URL in the browser to see the output of the application

If you get the message:
```
Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory
```
This means that you did not set up the `.flaskenv` described above


### Run on windows to get access to python
```
alias python='winpty /c/Users/cedlab/AppData/Local/Programs/Python/Python37/python.exe'
```
