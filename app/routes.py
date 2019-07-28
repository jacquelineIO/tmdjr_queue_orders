from flask import render_template, redirect, url_for
from app import app
from app.src.query_payments import get_list_payments
from app.src.process_payments import process_payments_response
from app.src.orders import get_orders, complete_order


@app.route('/')
@app.route('/index')
def index():
    payment_responses = get_list_payments()
    #print(payment_responses[0])
    process_payments_response(payment_responses)
    orders = get_orders()

    # Setup data for template
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

@app.route("/complete/<payment_id>/<part_num>")
def complete(payment_id, part_num):
    complete_order(payment_id, part_num)
    return redirect(url_for('index'))
