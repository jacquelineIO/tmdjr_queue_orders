from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.src.query_payments import get_list_payments
from app.src.process_payments import process_payments_response
from app.src.orders import get_orders, complete_order
from .models import clear_orders_table
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    orders = None
    if app.config['CONNECT_SQUAREAPI'] == False:
        orders = get_orders()

    # Not doing any special for use of USE_CANNED_TIMES_CONNECT_SQUAREAPI
    # therefore on multiple loads when using canned times there will
    # be failures

    if app.config['CONNECT_SQUAREAPI'] == False and orders.count() == 0:
        clear_orders_table()
        payment_responses = get_list_payments()
        process_payments_response(payment_responses)
    elif app.config['CONNECT_SQUAREAPI'] == True:
        payment_responses = get_list_payments()
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

@app.route("/complete/<payment_id>/<part_num>/")
@login_required
def complete(payment_id, part_num):
    complete_order(payment_id, part_num)
    return redirect(url_for('index'))

@app.route("/completepost", methods=["POST"])
@login_required
def completepost():
    if request.form:
        payment_id = request.form.get("payment_id")
        part_num = request.form.get("part_num")
        complete_order(payment_id, part_num)
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.lower()).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
