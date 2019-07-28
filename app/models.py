from app import db
from datetime import date, datetime, time
from pytz import timezone

# clear database
def clear_orders_table():
    try:
        num_rows_deleted = db.session.query(Order).delete()
        num_rows_deleted = db.session.query(OrderItem).delete()
        db.session.commit()
    except:
        db.session.rollback()

def run_today_central(last_run, today_central):
    last_run_central = last_run.astimezone(timezone('UTC'))
 
    if last_run_central.year == today_central.year and last_run_utc.month == today_central.month and last_run_central.day == today_central.day:
            return true
    else:
        if last_run_central.day < today_cental.day:
            clear_orders_table()
        return false

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    notes = db.Column(db.String(256))
    quantity = db.Column(db.Integer, default=1)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'),
        nullable=False)
    _modifiers = db.Column(db.String, default="")
    @property
    def modifiers(self):
        return [x for x in self._modifiers.split(';')]
    @modifiers.setter
    def modifiers(self, value):
        if self._modifiers is None:
            self._modifiers = value
        else:
            self._modifiers += ';%s' % value

    def __repr__(self):
        return '<Order Item {}>'.format(self.name)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_created_at = db.Column(db.DateTime, nullable=False)
    payment_id =  db.Column(db.String(128), index=True, unique=True)
    order_id = db.Column(db.String(10), nullable=False)
    itemizations = db.relationship('OrderItem', backref='order', lazy=True)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    part = db.Column(db.Integer, default=1)
    total_parts = db.Column(db.Integer, default=1)
    __table_args__ = (db.UniqueConstraint('payment_id', 'part', name='_paymentid_part_uc'),
            )

    def __repr__(self):
        return '<Order {}, payment_id {}, part_num {}>'.format(self.order_id, self.payment_id, self.part)

class LastRun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_run = db.Column(db.DateTime, nullable=False)

    def get_last_run(self):
        """Fetches rows from a Bigtable.

        Retrieve the last run timestamp from the table. If the table is 
        empty, then today's date will be returned. If the last run was not
        today's date then return today's date.

        Args:
            big_table: An open Bigtable Table instance.
            keys: A sequence of strings representing the key of each table row
                to fetch.
            other_silly_variable: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        Returns:
            A dict mapping keys to the corresponding table row data
            fetched. Each row is represented as a tuple of strings. For
            example:

            {'Serak': ('Rigel VII', 'Preparer'),
             'Zim': ('Irk', 'Invader'),
             'Lrrr': ('Omicron Persei 8', 'Emperor')}

            If a key from the keys argument is missing from the dictionary,
            then that row was not found in the table.

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
        """
        # Get timestamps for today in UTC timezone
        # Converting today's date from Central to UTC timezone
        now_central = datetime.now(timezone('US/Central'))
        today_central = now_central.replace(hour=0, minute=0, second=0, microsecond=0)
        today_utc = today_central.astimezone(timezone('UTC'))
        
        last_run_utc = self.query.all()
        if len(last_run_utc) == 0:
            return today_utc
        elif run_today_central(last_run_utc, today_central): 
            return last_run_utc[0].last_run
        else:
            return today_utc
