from app import app, db
from app.models import Order, OrderItem

def process_payments_response(payments_response):
    for payment in payments_response:
        print("for payment in payments_response")
        print(payment)
        order = Order()
        order_items = []
        for name, value in payment:
            if name == 'created_at':
                order.created_at = value
            elif name == 'id':
                order.payment_id = value
            elif name == 'itemizations':
                order_item = OrderItem()
                for item in value:
                    for item_name, item_value in item:
                        if item_name == 'name':
                            order_item.name = item_value
                        elif item_name == 'notes':
                            order_item.notes = item_value
                        elif item_name == 'modifiers':
                            for mod_name, mod_value in value:
                                if mod_name == 'name':
                                    order_item.modifiers(mod_value)
                        elif item_name == 'quantity':
                            order_item.quantity = item_value
                    order_items.append(order_item)
        order.itemizations = order_items
        order.order_id = order.payemnt_id[:4]
        db.session.add(order)
    db.session.commit()
