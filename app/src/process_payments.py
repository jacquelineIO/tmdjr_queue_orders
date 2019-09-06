# config:utf-8
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
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

def process_payments_response(payments_response):
    line_count_max = 14

    for payment in payments_response:
        #print("for payment in payments_response")
        #print(payment)
        order = Order()
        order_items = []
        part = 1
        line_count = 0

        fmt = "%Y-%m-%dT%H:%M:%SZ"
        order.part = part
        order.order_created_at = datetime.strptime(payment.created_at, fmt)
        order.payment_id = payment.id
        order.order_id = order.payment_id[:4]

        print("Creating TMDJ Order #{}".format(order.order_id))

        for item in payment.itemizations:
            line_count = line_count + 1  # add line for item.name

            if line_count > line_count_max:
                order.itemizations = order_items
                db.session.add(order)
                order = Order()
                order_items = []
                part = part + 1
                order.part = part

                order.order_created_at = datetime.strptime(payment.created_at, fmt)
                order.payment_id = payment.id
                order.order_id = order.payment_id[:4]
                line_count = 0

            #print("\twith part #{}".format(order.part))
            #print("\twith line #{}".format(line_count))
            order_item = OrderItem()
            order_item.name = item.name
            order_item.notes = item.notes
            #print("\tline item name {}".format(item.name))
            #print("\tline order_item name {}".format(order_item.name))
            if item.notes and item.notes.strip():
                line_count = line_count + 1
            order_item.quantity = item.quantity
            for mod in item.modifiers:
                order_item.modifiers = "+ " + mod.name.strip()
                line_count = line_count + 1
            order_items.append(order_item)

        order.itemizations = order_items
        db.session.add(order)
        try:
            db.session.commit()
            if part != 1:
                update_orders = Order.query.filter_by(payment_id=order.payment_id).update(dict(total_parts=part))
                db.session.commit()
        except (SQLAlchemyError, IntegrityError) as e:
            db.session.rollback()
            print("Except caught while committing order to database {}".format(e))
            print("Failed to add order {}".format(order))
