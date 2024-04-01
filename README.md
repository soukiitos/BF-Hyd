<center> <h1> BF-Hyd (Be Forever Hydrated) </center> </h1>
![BF-Hyd Logo](../static/images/BF-Hydlogo.jpg) 

## Description

BF-Hyd is an application that helps users track their daily water intake and reminds them to stay hydrated throughout the day. I chose this name to be simple and easy to spell and remember.

---

## Team

This is an individual project. I am Soukaina Lachheb, and I developed this project alone, taking it as a challenge.

| Repository | Files | Description |
|------------|-------|-------------|
|            |README.md|A README file containing the project's description|
|            |run.py | The main script of BF-Hyd, serving as its entry point. It includes:
|            |       | - Import statements  
|            |       | - Initialization of Flask App and Configuration  
|            |       | - Database Setup  
|            |       | - Mail Configuration  
|            |       | - Web Push Configuration  
|            |       | - Routes and View Functions  
|            |       | - Background Task Scheduling  
|            |       | - Execution of the Flask App |
|        |requirement.txt|A file containing all the required packages used in the project, generated using the command `pip freeze > requirements.txt`|
|    |setup_mysql.sql|A script creating a MySQL database named BFHyd_db and setting up a user account to access and manage this database|
|      |forms.py|A file containing form classes using Flask-WTF to define and handle web forms in a Flask application|
|    |alert.py|A script utilizing the Pushbullet API to send notifications to specified devices. It reads the content of a file named message.txt and sends a notification with its content to a specified device. The notification's title is set to "Please Remember"|
||message.txt|A file containing the message the user will receive|
||vapid_private.pem|A file likely containing a private key generated using the Elliptic Curve (EC) cryptography algorithm with the prime256v1 curve, used for VAPID (Voluntary Application Server Identification) authentication tokens|
||private_key.txt|Contains the Base64-encoded representation of the private key for VAPID authentication in web push notification systems|
||public_key.txt|Contains the Base64-encoded representation of the corresponding public key|
||__init__.py|A file signifying that the directory containing it is a Python package|
|models|user.py|Contains the definition of the User class, representing the structure of user data stored in the database|
|models|water_intake.py|Contains the definition of the WaterIntake class, representing the structure of WaterIntake data stored in the database|
|models| masscalculator.py|Contains the definition of the MassCalculatorData class, representing the structure of MassCalculatorData data stored in the database|
|models|__init__.py|Makes the db instance accessible throughout the package, facilitating database operations within the Flask application|
|static\css|.|Contains CSS files styling HTML elements, organizing HTML files, and providing a responsive design|
|static\script|.|Contains JavaScript files providing functionality and interactivity to HTML pages|
|static\images|.|Contains all images used in the project|
|templates|index.html|The homepage for BF-Hyd|
|templates|- about.html  
- age_calculate.html  
- contact.html  
- contact.html  
- heartLoader.html  
- index.html  
- login.html  
- mass_claculator.html  
- notification.html  
- water_intake.html  
- weather.html  
- X-ray.html|HTML files serving as templates for generating dynamic web pages in BF-Hyd|

## Installation

To install the required packages, run:
```bash
pip install -r requirements.txt
```