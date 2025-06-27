The Service Management System is a Django-based web application that allows customers to submit and track gas service requests online. It features user authentication, request tracking, an admin panel for management, and role-based access control. The system improves service efficiency, reduces wait times, and enhances customer experience for gas utility companies. 🚀🔥

![Screenshot](Output/Screenshot_1.png)

![Screenshot](Output/Screenshot_2.png)


Setup
Update the System
```bash
sudo apt-get update
```
To get this repository, run the following command inside your git enabled terminal

```bash
git clone https://github.com/sahilgunjal122/Service-Request-Portal.git
```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Download django using pip
```bash
sudo apt install python3-pip -y
```
Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```
```bash
pip install django
```
pip install -r requirements.txt
```bash
pip install -r requirements.txt
```
Once you have downloaded django, go to the cloned repo directory and run the following command
```bash
python3 manage.py makemigrations
```
This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
python3 manage.py migrate
```
One last step and then our App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
python3 manage.py createsuperuser
```
Start the server by following command
```bash
python3 manage.py runserver
```
Once the server is hosted, head over to http://127.0.0.1:8000/Service-Request-Portal for the App.

 📎API Endpoints
Token Authentication
POST /api/token-auth/
➤ Accepts username & password
➤ Returns a token

Public Endpoint
GET /api/public/
➤ Open to all

Protected Endpoint
GET /api/protected/
➤ Requires token in headers
➤ Returns current user's info

🤖 Telegram Bot Integration
Use @BotFather to create a bot

Add token in telegram_bot.py

Users who send /start will be saved into the database

Manually Sync /start Users:
```bash
python manage.py shell
>>> from request.telegram_bot import save_new_users
>>> save_new_users()
```
📬 Email Notifications
Sent after user registration

Sent after admin updates request status

Configured using Gmail SMTP

🧠 Technologies Used
Python 3.12

Django 5.2

Django REST Framework

SQLite (local database)

SMTP (Gmail)

Telegram Bot API


Cheers and Happy Coding :)
