"""
This function/component of the application should query the Square API function list_payments
periodically and upon loading the main queue URL. The complete button will trigger a refresh
of the orders queue.

Upon start of the application, the component should query all order from the beginning of the
day until the current time. On the next call to this function the begin_time should be the last
time the Square API will queried and the end_time should be the now current time.

This function should return the list of payments retrieved from the Square API function list_payments.
"""
from app import app, db
from app.models import LastRun, clear_orders_table
from app.queue_orders import get_squareapi_transaction_api, get_location
from app.src.test_data import load_test_data
from datetime import datetime
from pytz import timezone

def get_list_payments():
    if app.config['USE_CANNED_TIMES_CONNECT_SQUAREAPI'] == True:
        return get_list_payments_square_api_canned_times()
    elif app.config['CONNECT_SQUAREAPI'] == True:
        return get_list_payments_square_api()
    else:
        return get_list_payments_test_data()

def get_list_payments_square_api():
    
    # add your code here

    print ("Connecting to live SquareAPI")
    print ("Using UTC times begin_time {} and end_time {} to query api.list_payments".format(last_run_utc.strftime(fmt), now_utc.strftime(fmt)))

    # add your code here

def get_list_payments_square_api_canned_times():
    # Central Times
    begin_time = datetime.strptime(app.config['PAYMENTS_BEGIN_TIME'], '%Y-%b-%dT%H:%M:%S')
    begin_time_central = timezone('US/Central').localize(begin_time)
    end_time = datetime.strptime(app.config['PAYMENTS_END_TIME'], '%Y-%b-%dT%H:%M:%S')
    end_time_central = timezone('US/Central').localize(end_time)

    # Convert to UTC times
    begin_time_utc = begin_time_central.astimezone(timezone('UTC'))
    end_time_utc = end_time_central.astimezone(timezone('UTC'))
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    
    print ("Connecting to live SquareAPI")
    print ("Using CANNED UTC times begin_time {} and end_time {} to query api.list_payments".format(begin_time_utc.strftime(fmt), end_time_utc.strftime(fmt)))

    # clear table when using canned times, can't have duplicate payments ID in tables
    clear_orders_table()

    # Connect to Square
    api = get_squareapi_transaction_api()
    location = get_location()
    try:
        api_response = api.list_payments(location_id=location, begin_time=begin_time_utc.strftime(fmt) , end_time=end_time_utc.strftime(fmt))
        #print (api_response)
        return api_response
    except ApiException as e:
        print ('Exception when calling TransactionsApi->list_transactions: %s\n' % e)
        return []

def get_list_payments_test_data():
    # clear table when using testing data, can't have duplicate payments ID in tables
    clear_orders_table()
    print ("Using Test Data")
    payment_responses = load_test_data()
    return payment_responses
