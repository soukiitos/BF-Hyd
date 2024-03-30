import logging
import json
import os
import requests

from flask import request, Response, render_template, jsonify, Flask, redirect, url_for, flash
from pywebpush import webpush, WebPushException
from models.user import User
from models.water_intake import WaterIntake
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from flask_mail import Mail, Message
from forms import loginForm, SigninForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kiitos23456TrueNotYaw'
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587  # Port for SMTP (587 is typical for TLS)
app.config['MAIL_USE_TLS'] = True  # Enable TLS
app.config['MAIL_USERNAME'] = 'bfhyd24@gmail.com'
app.config['MAIL_PASSWORD'] = 'kiitos2024bfhyd24'
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

# Initialize Marshmallow
ma = Marshmallow(app)

def send_web_push(subscription_information, message_body):
    return webpush(
        subscription_info=subscription_information,
        data=message_body,
        vapid_private_key=VAPID_PRIVATE_KEY,
        vapid_claims=VAPID_CLAIMS
        )

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
    login_form = SigninForm(request.form)
    email = request.form.get('email')
    password = request.form.get('password')

    # Query the database for the user with the provided email
    user = User.query.filter_by(email=email).first()

    # Check if the user exists and if the password is correct
    if user and user.check_password(password):
        # Authentication successful, redirect to the homepage
        return render_template('/')
    else:
        # Display error message if user does not exist
        flash('Invalid email or password. Please try again. If you are not signed up, Sign Up First', 'error')
        return redirect(url_for('login'))

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

@app.route('/mass_calculator')
def mass_claculator():
    return render_template('mass_claculator.html')

@app.route('/Weather')
def weather():
    # Mock weather data
    mock_weather_data = [
        {
            'city': 'Kenitra',
            'temperature': '25°C',
            'description': 'Sunny',
            'humidity': '50%',
            'wind_speed': '10 km/h',
        },
        {
            'city': 'Rabat',
            'temperature': '29°C',
            'description': 'Sunny',
            'humidity': '35%',
            'wind_speed': '2 km/h', 
        },
        {
            'city': 'Paris',
            'temperature': '27°C',
            'description': 'Sunny',
            'humidity': '34%',
            'wind_speed': '0 km/h',
        },
        {
            'city': 'New York',
            'temperature': '9°C',
            'description': 'cloud-rain',
            'humidity': '23%',
            'wind_speed': '14 km/h',
        }
    ]
    date = 'Monday, 01 April 2024'

    # Prepare the weather data for rendering in the HTML template
    weather_data_for_html = [
        {
            'date': date,
            'city': data['city'],
            'temperature': data['temperature'],
            'description': data['description'],
            'humidity': data['humidity'],
            'wind_speed': data['wind_speed'],
        } for data in mock_weather_data
    ]

    return render_template('weather.html', weather_data=weather_data_for_html)

@app.route('/send_email')
def send_email():
    msg = Message('Subject of the Email', recipients=['example@gmail.com'])
    msg.body = "Hello mate, it's time to get you're water. don't forget to be always hydrated"
    mail.send(msg)
    return 'Email sent successfully'

@app.route('/contact')
def contact():
    return render_template('contact.html')
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)