from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, FloatField, TextAreaField, SubmitField, SelectField
from wtforms import DateField
from wtforms import IntegerField, RadioField
from wtforms.validators import InputRequired, NumberRange, Length


class loginForm(FlaskForm):
    # UserForm class
    user_id = StringField('User ID')
    username = StringField('Name')
    email = StringField(' User mail')
    password = StringField('Password')
    
    submit = SubmitField('SIGN UP')


class SigninForm(FlaskForm):
    user_id = StringField('User ID')
    email = StringField(' User mail')
    password = StringField('Password')
    
    submit = SubmitField('SIGN IN')
    
    
class WaterIntakeForm(FlaskForm):
    user_id = FloatField('User ID', validators=[InputRequired(), Length(max=50)])
    amount = FloatField('Amount (in liters)', validators=[InputRequired(), NumberRange(min=0)])
    date = DateField('Date', validators=[InputRequired()])

class MassCalculatorForm(FlaskForm):
    age = IntegerField('Age', validators=[InputRequired(), NumberRange(min=0)])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[InputRequired()])
    height = FloatField('Height (cm)', validators=[InputRequired(), NumberRange(min=0)])
    weight = FloatField('Weight (kg)', validators=[InputRequired(), NumberRange(min=0)])