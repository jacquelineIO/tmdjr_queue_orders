from app import app 
from app.models import LastRun
from app.queue_orders import get_squareapi_transaction_api, get_location
from datetime import datetime

def get_list_payments():
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    last_run = LastRun()
    last_run_utc = last_run.get_last_run()
    now_utc = datetime.utcnow()
    print(last_run_utc)
    api = get_squareapi_transaction_api()
    location = get_location()
    try:
        api_response = api.list_payments(location_id=location, begin_time=last_run_utc.strftime(fmt) , end_time=now_utc.strftime(fmt), limit=1)
        print (api_response)
    except ApiException as e:
        print ('Exception when calling TransactionsApi->list_transactions: %s\n' % e)
