import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Access the SquarePOS API
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN') or 'you-will-never-guess'
    TMDJR_LOCATION = os.environ.get('LOCATION_ID')
    # Configure the database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
