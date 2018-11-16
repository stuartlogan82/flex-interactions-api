from . import db

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    interactions = db.relationship('Interaction', backref='customer', lazy='dynamic')

    def __repr__(self):
        return '<Customer %r>' % self.first_name

class Interaction(db.Model):
    __tablename__ = 'interactions'
    id = db.Column(db.Integer, primary_key=True)
    conference_sid = db.Column(db.String(64), nullable=True)
    date_created = db.Column(db.String(64), nullable=True)
    customer_name = db.Column(db.String(64) ,nullable=True)
    worker_name = db.Column(db.String(64), nullable=True)
    recording_url = db.Column(db.String(64), nullable=True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    chat_channel = db.Column(db.String(64), nullable=True)
    interaction_type = db.Column(db.String(64), nullable=True)
    duration = db.Column(db.Time, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.customer_name