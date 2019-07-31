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
    for payment in payments_response:
        #print("for payment in payments_response")
        #print(payment)
        order = Order()
        order_items = []
        fmt = "%Y-%m-%dT%H:%M:%SZ"
        order.order_created_at = datetime.strptime(payment.created_at, fmt)
        order.payment_id = payment.id

        for item in payment.itemizations:
            order_item = OrderItem()
            order_item.name = item.name
            order_item.notes = item.notes
            order_item.quantity = item.quantity
            for mod in item.modifiers:
                order_item.modifiers = "+ " + mod.name
            order_items.append(order_item)

        order.itemizations = order_items
        order.order_id = order.payment_id[:4]
        try:
            db.session.add(order)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            print("Except caught while commiting order to database {}".format(e))
            print("Failed to add order {}".format(order))
