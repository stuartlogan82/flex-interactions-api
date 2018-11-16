from flask import Flask, render_template
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))

def make_shell_context():
    return dict(app=app, db=db, Customer=Customer, Interaction=Interaction)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    return '<h1>API Running!</h1>'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# Model definition

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

if __name__ == '__main__':
    manager.run()
