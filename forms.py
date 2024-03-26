from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, FloatField, TextAreaField, SubmitField, SelectField


class loginForm(FlaskForm):
    # UserForm class
    user_id = StringField('User ID')
    username = StringField('Name')
    email = StringField(' User mail')
    password = StringField('Password')
    
    submit = SubmitField('SIGN UP')