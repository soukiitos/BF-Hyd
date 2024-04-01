<center> <h1> BF-Hyd (Be Forever Hydrated) </center> </h1>
<center><img src="../static/images/BF-Hydlogo.jpg"></center>

<h3>Description</h2>

BF-Hyd is an application that help the users to track their daily water and reminds them to stay hydrated through the day, i choose this name to be simple and can spell it and memorize it easily
---

<h3>Team </h3>

This is an individual project, I am Soukaina Lachheb I did all this project alone, i tried to take it as a challenge.

| Repository | Files | Description |
|------------|-------|-------------|
|            |README.md|A README file that contains all description of this project|
|            |run.py | Serves as the entry point for BF-Hyd or i can say the main script of it, contains:  
- Import Statements  
- Initialization of Flask App and Configuration  
- Database Setup  
- Mail Configuration  
- Web Push Configuration  
- Routes and View Functions  
- Background Task Scheduling  
- Execution of the Flask App 
|        |requirement.txt|Contains all the requirement package used in this project, to get i used the command: pip freeze > requirements.txt|
|    |setup_mysql.sql|This script creates a MySQL database named BFHyd_db and sets up a user account to access and manage this database|
|      |forms.py|This file likely contains form classes using Flask-WTF to define and handle web forms in a Flask application|
|    |alert.py|This script utilizes the Pushbullet API to send a notification to specified devices so it reads the content of a file named message.txt, then uses the Pushbullet API to send a notification with the content of that file to a specified device. The notification's title is set to "Please Remember"|
||message.txt|This file Contains the Message the user will recieve|
||vapid_private.pem|This file likely contains a private key generated using the Elliptic Curve (EC) cryptography algorithm with the prime256v1 curve, also known as the NIST P-256 or secp256r1 curve. This key is commonly used in web push notification systems for generating VAPID (Voluntary Application Server Identification) authentication tokens|
||private_key.txt|contains its Base64-encoded representation, which can be used for VAPID authentication in web push notification systems|
||public_key.txt|contains the Base64-encoded representation of the corresponding public key|
||__init__.py|this file presence signifies that the directory containing it is a Python package|
|models|user.py|contains the definition of the User class, which represents the structure of the user data stored in the database|
|models|water_intake.py|contains the definition of the WaterIntake class, which represents the structure of the WaterIntake data stored in the database|
|models| masscalculator.py|contains the definition of the MassCalculatorData class, which represents the structure of the MassCalculatorData data stored in the database|
|models|__init__.py|This file make the db instance becomes accessible throughout the package and can be imported into other modules within the package. This allows models to be defined using SQLAlchemy and facilitates database operations within the Flask application|
|static\css|- weather.css  
- water_intake.css  
- style_notification.css  
- style_Age.css  
- styleX.css  
- style.css 
- about.css  
- contact.css  
- HLoaderstyle.css  
- login.css  
- mass_calculator.css  
|This files style the HTML elements, Contain Frameworks and Libraries, Organize the html files, help to give a Responsive Design|
|static\script|- about.js  
- contact.js  
- login.js  
- main.js  
- mass_calculator.js  
- notification.js  
- script1.js  
- scriptX.js  
- sw.js  
- water_intake.js  
- weather.js||
|static\images|.|This folder contains all the images used in this project|
|templates|index.html|is the homepage for BF-Hyd|
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
- X-ray.html|Are HTML files that serve as templates for generating dynamic web pages in BF-Hyd|




# if You Wanna :::

pip install -r requirements.txt


