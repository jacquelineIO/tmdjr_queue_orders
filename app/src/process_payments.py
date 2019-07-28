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
        db.session.add(order)
    db.session.commit()
