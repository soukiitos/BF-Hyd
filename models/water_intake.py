from flask_marshmallow import Marshmallow
from datetime import datetime
from . import db

# Create an instance of Marshmallow
ma = Marshmallow()

class WaterIntake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, user_id, amount, date):
        self.user_id = user_id
        self.amount = amount
        self.date = date


# Define schema for WaterIntake model
class WaterIntakeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WaterIntake

# Instantiate schema
water_intake_schema = WaterIntakeSchema()