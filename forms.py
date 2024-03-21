from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, FloatField, TextAreaField, SubmitField, SelectField


class loginForm(FlaskForm):
    # UserForm class
    user_id = StringField('User ID')
    username = StringField('User Name')
    First_name = StringField('First Name')
    last_name = StringField('Last Name')
    birthdate = StringField('Birth Date')
    email = StringField(' User mail')
    phone_number = StringField('Phone Number')
    password = StringField('Password')
    
    submit = SubmitField('Submit User')