from datetime import datetime
from . import db

class WaterIntake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, user_id, amount, date):
        self.user_id = user_id
        self.amount = amount
        self.date = date