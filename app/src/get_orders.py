from app import app
from app.models import Order, OrderItem
from sqlalchemy import desc

def get_orders():
    orders = Order.query.filter_by(completed=False).order_by(desc(Order.order_created_at))
    return orders
