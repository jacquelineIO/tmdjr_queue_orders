from app import app, db
from app.models import Order, OrderItem
from sqlalchemy import desc

def get_orders():
    orders = Order.query.filter_by(completed=False).order_by(desc(Order.order_created_at))
    return orders

def complete_order(payment_id, part_num):
    order_to_complete = Order.query.filter_by(payment_id=payment_id, part=part_num)
    if order_to_complete.count() > 0:
        order_to_complete[0].completed = True
        print("Order {} marked completed {}".format(order_to_complete[0].order_id, order_to_complete[0].part))

    db.session.commit()
    db.session.flush()

