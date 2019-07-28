from app import app
import squareconnect
from squareconnect.rest import ApiException
#from squareconnect.apis.transactions_api import TransactionsApi
from squareconnect.apis.v1_transactions_api import V1TransactionsApi
from pytz import timezone
from datetime import datetime

def get_squareapi_transaction_api():
    # create an instance of the Location API class
    #api_instance = TransactionsApi()
    api_instance = V1TransactionsApi() 
    # setup authorization
    api_instance.api_client.configuration.access_token = app.config['ACCESS_TOKEN']
    return api_instance

def get_location():
    return app.config['TMDJR_LOCATION']
