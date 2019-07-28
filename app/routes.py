from flask import render_template
from app import app
from app.src.query_payments import get_list_payments
from app.src.process_payments import process_payments_response
from app.src.test_data import load_test_data
from app.src.get_orders import get_orders
from app.models import clear_orders_table


@app.route('/')
@app.route('/index')
def index():
    # get_list_payments() is connecting to live data
    # commementing out for now and using test data
    #payment_responses = get_list_payments()

    # temporary delete orders table on request because
    # we are not getting new data with the test data and
    # the application with fail with duplicates
    clear_orders_table()
    payment_responses = load_test_data()
    #print(payment_responses[0])
    process_payments_response(payment_responses)
    orders = get_orders()
    next_queue = []
    active_order = None
    preview_order = None
    if orders.count() > 0:
        active_order = orders[0]
    if orders.count() > 1:
        preview_order = orders[1]
        for i, order in enumerate(orders):
            if i != 0:
                next_queue.append(order.order_id)

    print(active_order)
    print(preview_order)
    print(next_queue)
    
    return render_template('index.html', title='Home', active_order=active_order, preview_order=preview_order, next_queue=next_queue)
