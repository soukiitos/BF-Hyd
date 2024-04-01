import logging
import json
import os
import requests
import atexit

from flask import request, Response, render_template, jsonify, Flask, redirect, url_for, flash
from pywebpush import webpush, WebPushException
from models.user import User
from models.water_intake import WaterIntake
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from flask_mail import Mail, Message
from forms import loginForm, SigninForm, MassCalculatorForm
from forms import WaterIntakeForm
from models.masscalculator import MassCalculatorData

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kiitos23456TrueNotYaw'

DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH = os.path.join(os.getcwd(), "private_key.txt")
DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH = os.path.join(os.getcwd(), "public_key.txt")

VAPID_PRIVATE_KEY = open(DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH, "r+").readline().strip("\n")
VAPID_PUBLIC_KEY = open(DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH, "r+").read().strip("\n")

VAPID_CLAIMS = {
    "sub": "bfhyd24@gmail.com"
}

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://BFHyd:kiitos@localhost/BFHyd_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Mail
mail = Mail(app)

# Initialize Marshmallow
ma = Marshmallow(app)

def send_email():
    with app.app_context():
        from models.user import User
        users = User.query.all()
        for user in users:
            msg = Message('Daily Reminder', recipients=[user.email])
            msg.body = "Hello {}, it's time to drink water and stay hydrated!".format(user.username)
            mail_send(msg)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Port for SMTP (587 is typical for TLS)
app.config['MAIL_USE_TLS'] = True  # Enable TLS
app.config['MAIL_USERNAME'] = 'bfhyd24@gmail.com'
app.config['MAIL_PASSWORD'] = 'cnuqnlyizrmboqfg'


def send_web_push(subscription_information, message_body):
    return webpush(
        subscription_info=subscription_information,
        data=message_body,
        vapid_private_key=VAPID_PRIVATE_KEY,
        vapid_claims=VAPID_CLAIMS
        )

@app.route('/test_send_email')
def test_send_email():
    send_email()  # Trigger the send_email function
    return 'Test email sent successfully!'

# API Endpoint to Add Water Intake
@app.route('/water_intake', methods=['GET', 'POST'])
def water_intake():
    if request.method == 'POST':
        user_id = request.json.get('user_id')
        amount = request.json.get('amount')
        date_str = request.json.get('date')

        if user_id is None or amount is None or date_str is None:
            return jsonify({'error': 'Missing user_id, amount, or date'}), 400

        # Validate and parse date
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

        # Create new water intake record
        new_water_intake = WaterIntake(user_id, amount, date)
        db.session.add(new_water_intake)
        db.session.commit()

        return water_intake_schema.jsonify(new_water_intake)
    elif request.method == 'GET':
        user_id = request.args.get('user_id')  # assuming user_id is passed as a query parameter
        if user_id is None:
            return jsonify({'error': 'Missing user_id parameter in the request'}), 400

        water_intakes = WaterIntake.query.filter_by(user_id=user_id).all()
        return jsonify(water_intakes_schema.dump(water_intakes))

# Route to render the Water Intake page
@app.route('/water_intake_page')
def water_intake_page():
    return render_template('water_intake.html')

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET'])
def login():
    login_form = SigninForm()
    signup_form = loginForm()
    return render_template('login.html', signup_form=signup_form, login_form=login_form)

@app.route('/signup', methods=['POST'])
def signup():
    signup_form = loginForm(request.form)

    if signup_form.validate_on_submit():
        new_user = User(
            username=signup_form.username.data,
            email=signup_form.email.data,
            password=signup_form.password.data,
            )

        # Add the new user to the database
        db.session.add(new_user)
        # Commit the session to save the user
        db.session.commit()

    flash('Registration Successful. You can now login.', 'success')
    return redirect(url_for('login'))

    return render_template('login.html', signup_form=signup_form)

@app.route('/signin', methods=['POST'])
def signin():
    signin_form = SigninForm(request.form)
    email = request.form.get('email')
    password = request.form.get('password')

    # Query the database for the user with the provided email
    user = User.query.filter_by(email=email).first()

    # Check if the user exists and if the password is correct
    if user and user.check_password(password):
        # Authentication successful, redirect to the homepage
        return redirect(url_for('index'))
    else:
        # Display error message if user does not exist
        flash('Invalid email or password. Please try again. If you are not signed up, Sign Up First', 'error')
        return redirect(url_for('login'))
    return render_template('index')

@app.route('/notification')
def notification():
    return render_template('notification.html')

@app.route('/subscription/', methods=["GET", "POST"])
def subscription():
    if request.method == "GET":
        return Response(
            response=json.dumps({"public_key": VAPID_PUBLIC_KEY}),
            headers={"Access-Control-Allow-Origin": "*"}, content_type="application/json"
            )
            
    subscription_token = request.json.get("subscription_token")
    return Response(status=201, mimetype="application/json")

@app.route("/push_v1/", methods=['POST'])
def push_v1():
    message = "Hello!! Mate! Drink Your water Now and stay Healty.\n  Have a Great Day:)"
    print("is_json", request.is_json)
    
    if not request.json or not request.json.get('sub_token'):
        return jsonify({'failed': 1})
        
    token = request.json.get('sub_token')
    try:
        token = json.loads(token)
        send_web_push(token, message)
        return jsonify({'success': 1})
    except Exception as e:
        print("error", e)
        return jsonify({'failed': str(e)})

@app.route('/age_calculate')
def age_calculate():
    return render_template('age_calculate.html')

@app.route('/X-ray')
def x_ray():
    return render_template('X-ray.html')

@app.route('/heartLoader')
def heart_loader():
    return render_template('heartLoader.html')

@app.route('/mass_calculator', methods=['GET', 'POST'])
def mass_calculator():
    form = MassCalculatorForm()
    
    if form.validate_on_submit():
        age = form.age.data
        gender = form.gender.data
        height = form.height.data
        weight = form.weight.data

        # Create a new MassCalculatorData instance and store it in the database
        new_data = MassCalculatorData(age=age, gender=gender, height=height, weight=weight)
        db.session.add(new_data)
        db.session.commit()

        flash('Data submitted successfully!', 'success')
        return redirect(url_for('mass_calculator'))
        
    return render_template('mass_claculator.html', form=form)

@app.route('/Weather')
def weather():
    # I already done the weather API at weather.js
    return render_template('weather.html')

@app.route('/contact')
def contact():
    # I already fix the sending msg from the users: so it's all fixed
    return render_template('contact.html')
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    # Schedule the task to run daily
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_email, 'cron', hour=8, minute=10)  # Send email daily at 08:10
    scheduler.start()
    
    # Stop the scheduler when the Flask app exits
    atexit.register(lambda: scheduler.shutdown())
    
    app.run(debug=True)