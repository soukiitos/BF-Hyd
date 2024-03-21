import logging
import json
import os
import requests

from flask import request, Response, render_template, jsonify, Flask
from pywebpush import webpush, WebPushException
from forms import loginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Kiitos23456TrueNotYaw'

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    form = loginForm()

    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            birthdate=form.birthdate.data,
            email=form.email.data,
            phone_number=form.phone_number.data,
            password=form.password.data,
        )
        
        # Save the new user to the database
        db.session.add(new_user)
        db.session.commit()
        
        
        return render_template('login.html')
    
    return render_template('login.html', form=form)

@app.route('/notification')
def notification():
    DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH = os.path.join(os.getcwd(), "private_key.txt")
    DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH = os.path.join(os.getcwd(), "public_key.txt")
    
    VAPID_PRIVATE_KEY = open(DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH, "r+").readline().strip("\n")
    VAPID_PUBLIC_KEY = open(DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH, "r+").read().strip("\n")
    
    VAPID_CLAIMS = {
        "sub": "mailto:develop@raturi.in"
        }
        
    def send_web_push(subscription_information, message_body):
        return webpush(
            subscription_info=subscription_information,
            data=message_body,
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims=VAPID_CLAIMS
            )
            
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
    message = "Push Test v1"
    
    if not request.json or not request.json.get('sub_token'):
        return jsonify({'failed': 1})
        
    token = request.json.get('sub_token')
    try:
        token = json.loads(token)
        send_web_push(token, message)
        return jsonify({'success': 1})
    except Exception as e:
        app.logger.error("Error sending push notification: %s", e)
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
    mock_weather_data = {
        'city': 'Kenitra City',
        'temperature': '25°C',
        'description': 'Partly cloudy',
        'humidity': '50%',
        'wind_speed': '10 km/h',
        }

    return render_template('weather.html', weather_data=mock_weather_data)
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)