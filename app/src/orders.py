from app import app, db
from app.models import Order, OrderItem
from sqlalchemy import desc

def get_orders():
    db.session.flush()
    orders = Order.query.filter_by(completed=False).order_by(desc(Order.order_created_at))
    return orders

def complete_order(payment_id, part_num):
    #Order.query.filter_by(payment_id=payment_id, part=part_num).update({"completed":True})
    order_to_complete = Order.query.filter_by(payment_id=payment_id, part=part_num)
    order_to_complete.completed = True
    db.session.commit()
    db.session.flush()

