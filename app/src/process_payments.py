"""
This function/component of the application should parse the input (list of payments from call to Square API 
function list_payments) and store the needed fields of information into a new Orders object and append 
the Orders object to a list. This list will be returned from this function and used for displaying the order
information on the screen. The list of orders will be sorted in descending order by using the 
field ‘created_at’.

The order_id will be the first 4 characters  of the  payment id and used as-is (keeping the current case).
"""
from datetime import datetime
from app import app, db
from app.models import Order, OrderItem

def process_payments_response(payments_response):

