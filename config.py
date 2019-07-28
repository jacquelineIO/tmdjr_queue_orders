import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # If CONNECT_SQUAREAPI is false, then application will be in test mode
    print("Config os.environ.get('CONNECT_SQUAREAPI') = {}".format(os.environ.get('CONNECT_SQUAREAPI')))
    CONNECT_SQUAREAPI = False
    if os.environ.get('CONNECT_SQUAREAPI') == '1':
        CONNECT_SQUAREAPI = True
    print("CONNECT_SQUAREAPI={}".format(CONNECT_SQUAREAPI))

    # If CONNECT_SQUAREAPI is true then check if we are using canned times
    USE_CANNED_TIMES_CONNECT_SQUAREAPI = False
    if CONNECT_SQUAREAPI == True and os.environ.get('USE_CANNED_TIMES_CONNECT_SQUAREAPI') == '1':
        USE_CANNED_TIMES_CONNECT_SQUAREAPI = True
        PAYMENTS_BEGIN_TIME = os.environ.get('PAYMENTS_BEGIN_TIME') 
        PAYMENTS_END_TIME = os.environ.get('PAYMENTS_END_TIME')
        print("USE_CANNED_TIMES_CONNECT_SQUAREAPI={}".format(USE_CANNED_TIMES_CONNECT_SQUAREAPI))
        print("PAYMENTS_BEGIN_TIME {}, PAYMENTS_END_TIME {}".format(PAYMENTS_BEGIN_TIME, PAYMENTS_END_TIME))
        
    # Access the SquarePOS API
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN') or 'you-will-never-guess'
    TMDJR_LOCATION = os.environ.get('LOCATION_ID')

    # Configure the database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
