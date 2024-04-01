<center>
    <h1> BF-Hyd (Be Forever Hydrated)</h1>
</center>  

#### The personal mail:
[soukainalachheb93@gmail.com]()

#### The BF-Hyd mail: 
[bfhyd24@gmail.com]()
  
<p align="center">
  <img src="static/images/BF-Hydlogo.jpg" width="600" border-radius="30%">
</p>

## Description

BF-Hyd is an application that helps users track their daily water intake and reminds them to stay hydrated throughout the day. I chose this name to be simple and easy to spell and remember. and also there are other topics in this project like help the user to calculate their age, and Calculate their Body Mass Index... etc, and also there is a small weather application beautifull and cute. I hope you all like [This Project](https://github.com/soukiitos/BF-Hyd), BF-Hyd offers a diverse range of functionalities to promote user engagement and well-being.

---

## Team
- Soukaina Lachheb  

I developed BF-Hyd as an individual project, driven by my passion for health and technology. It has been a challenging yet rewarding journey, and I am proud to share the results with you.  
  

------------------------------------
| Repository | Files | Description |
|------------|-------|-------------|
|            |[README.md](https://github.com/soukiitos/BF-Hyd/blob/main/README.md)|A README file containing the project's description|
|            |[run.py](https://github.com/soukiitos/BF-Hyd/blob/main/run.py)| The main script of BF-Hyd, serving as its entry point. It includes:
|            |       | - Import statements  
|            |       | - Initialization of Flask App and Configuration  
|            |       | - Database Setup  
|            |       | - Mail Configuration  
|            |       | - Web Push Configuration  
|            |       | - Routes and View Functions  
|            |       | - Background Task Scheduling  
|            |       | - Execution of the Flask App |
|        |[requirement.txt](https://github.com/soukiitos/BF-Hyd/blob/main/requirements.txt)|A file containing all the required packages used in the project, generated using the command `pip freeze > requirements.txt`|
|    |[setup_mysql.sql](https://github.com/soukiitos/BF-Hyd/blob/main/setup_mysql.sql)|A script creating a MySQL database named BFHyd_db and setting up a user account to access and manage this database|
|      |[forms.py](https://github.com/soukiitos/BF-Hyd/blob/main/forms.py)|A file containing form classes using Flask-WTF to define and handle web forms in a Flask application|
|    |[alert.py](https://github.com/soukiitos/BF-Hyd/blob/main/alert.py)|A script utilizing the Pushbullet API to send notifications to specified devices. It reads the content of a file named message.txt and sends a notification with its content to a specified device. The notification's title is set to "Please Remember"|
||[message.txt](https://github.com/soukiitos/BF-Hyd/blob/main/message.txt)|A file containing the message the user will receive|
||vapid_private.pem|A file likely containing a private key generated using the Elliptic Curve (EC) cryptography algorithm with the prime256v1 curve, used for VAPID (Voluntary Application Server Identification) authentication tokens|
||private_key.txt|Contains the Base64-encoded representation of the private key for VAPID authentication in web push notification systems|
||public_key.txt|Contains the Base64-encoded representation of the corresponding public key|
||[__init__.py](https://github.com/soukiitos/BF-Hyd/blob/main/__init__.py)|A file signifying that the directory containing it is a Python package|
|[models](https://github.com/soukiitos/BF-Hyd/tree/main/models)|user.py|Contains the definition of the User class, representing the structure of user data stored in the database|
|[models](https://github.com/soukiitos/BF-Hyd/tree/main/models)|water_intake.py|Contains the definition of the WaterIntake class, representing the structure of WaterIntake data stored in the database|
|[models](https://github.com/soukiitos/BF-Hyd/tree/main/models)| masscalculator.py|Contains the definition of the MassCalculatorData class, representing the structure of MassCalculatorData data stored in the database|
|[models](https://github.com/soukiitos/BF-Hyd/tree/main/models)|__init__.py|Makes the db instance accessible throughout the package, facilitating database operations within the Flask application|
|[static\css](https://github.com/soukiitos/BF-Hyd/tree/main/static/css)|.|Contains CSS files styling HTML elements, organizing HTML files, and providing a responsive design|
|[static\script](https://github.com/soukiitos/BF-Hyd/tree/main/static/script)| . |Contains JavaScript files providing functionality and interactivity to HTML pages|
|[static\images](https://github.com/soukiitos/BF-Hyd/tree/main/static/images)|.|Contains all images used in the project|
|[templates](https://github.com/soukiitos/BF-Hyd/tree/main/templates)|[index.html](https://github.com/soukiitos/BF-Hyd/blob/main/templates/index.html)|The homepage for BF-Hyd|
|[templates](https://github.com/soukiitos/BF-Hyd/tree/main/templates)| . |HTML files serving as templates for generating dynamic web pages in BF-Hyd|

## Virtual Environnement

I named the virtual environnemet [BF-Hyd](), to create it i used the command:
```command
python -m venv BF-Hyd
```  
and to activate it i used the command:
```command
BF-Hyd\Scripts\activate
```  
to deactivate it:
```command
deactivate
```  

## Installation

To install the required packages, run:
```bash
pip install -r requirements.txt
```

## Some BF-Hyd Pages Images:

- The [homepage]((https://github.com/soukiitos/BF-Hyd/blob/main/templates/index.html)) here is a snippest of how it looks like:
<p align="center">
  <img src="static/images/index_cap.png" width="400">
</p>  

- I used a card to talk a bit about my portfolio and give a small Description of this project, and some of languages i used, here is the about card:  

<p align="center">
  <img src="static/images/about.png" width="400">
</p>  

- I tried to bring the user closer to the application, so i created [Contact Us](https://github.com/soukiitos/BF-Hyd/blob/main/templates/contact.html) form to communicate with us: here is a how it looks like:
<p align="center">
  <img src="static/images/contact_cap1.png" width="400">
</p>
<p align="center">
  <img src="static/images/contact_cap2.png" width="400">
</p> 

- Of course we must do a login form, so when he sign up with us, he'll get a daily notification in his phone, so here is how the Sign In/ Sign Up form looks like:  
<p align="center">
  <img src="static/images/login-cap.png" width="400">
</p>

- And here is how the notification looks like:  
<p align="center">
  <img src="static/images/alert-test.jpg" width="400">
</p>

- I tried to make the user love this application and visit it time by time, i did a age calculator and Mass Body Calculator forms, here are how they look like:  

<p align="center">
  <img src="static/images/ageCal-cap.png" width="400">
</p>
<p align="center">
  <img src="static/images/BodyMassCal_cap.png" width="400">
</p>  

- I did a small Weather Application, so we know that the weather is related to hydration, that's why i wanted to make the user aware of everything to stay healthy. here is how the app looks like:  
<p align="center">
  <img src="static/images/weather_cap.png" width="400">
</p>  

- To make this app funny, i wanted the user to discover a lot of things and make hiw enjoy visiting it, i did a Virtuel X-ray Experience, here is how it looks like:
<p align="center">
  <img src="static/images/X-ray_cap.png" width="400">
</p>

## API'S:

So for the api's i tried to find the api's as possible, so:  
- for the WEATHERAPI i used this mail[https://openweathermap.org/](https://openweathermap.org/), i create my account and get My API Keys, then i choose the API call:  
```bash
https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${APIKey}
```

- So for the notificationn i tred Three ways to send messages, so first one i used: PushBullet[https://www.pushbullet.com/](https://www.pushbullet.com/) i created my own account in it too, i set the settigs and access key, and i get my APIKey, then i linked it with [alert.py](https://github.com/soukiitos/BF-Hyd/blob/main/alert.py) and [message.txt](https://github.com/soukiitos/BF-Hyd/blob/main/message.txt) to Pythonanywhere [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/) so in pythonanywhere i set the database, and tasks where Schedule tasks(!!I tried just the free users)

- For /send_message, i set the SMTP to set the connection between the application and users at a scheduled time, i set the SMTP at the mail 'bfhyd24@gmail.com', here is the configuration in run.py:
```bash
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Port for SMTP (587 is typical for TLS)
app.config['MAIL_USE_TLS'] = True  # Enable TLS
app.config['MAIL_USERNAME'] = 'bfhyd24@gmail.com'
app.config['MAIL_PASSWORD'] = 'PASSWORDGIVEN'
``` 
and sheduled the time like here :
```
# Schedule the task to run daily
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_email, 'cron', hour=8, minute=10)  # Send email daily at 08:10
    scheduler.start()
    
    # Stop the scheduler when the Flask app exits
    atexit.register(lambda: scheduler.shutdown())
```

## Frameworks
- W3C [https://www.w3.org](https://www.w3.org/)
- sweetalert2[https://sweetalert2.github.io](https://sweetalert2.github.io/)
- Box Icons [https://boxicons.com/](https://boxicons.com/)
- Bootsrap [https://icons.getbootstrap.com/](https://icons.getbootstrap.com/)

## Run Mode:`
to run this project in local, i tried the command:
```bash
flask run
```

it shows like this:
```
flask run
 * Serving Flask app 'run.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

## DataBase Configuration:
```
# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://BFHyd:kiitos@localhost/BFHyd_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

I setup mysql with a file i named it with [setup_mysql.sql](https://github.com/soukiitos/BF-Hyd/blob/main/setup_mysql.sql)

```
mysql -u BFHyd -p
Enter password: ******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 76
Server version: 8.0.31 MySQL Community Server - GPL

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |  
+--------------------+  
| bfhyd_db           |  
| information_schema |  
| performance_schema |  
+--------------------+  
3 rows in set (0.03 sec)
```

## Conclusion:
In conclusion, I hope that BF-Hyd will serve as a useful tool for users seeking to improve their hydration habits and overall health. Thank you for taking the time to explore this project, and I welcome any feedback or contributions to further enhance its capabilities.