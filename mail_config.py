# config.py
from flask import Flask
from flask_mail import Mail, Message

app_mail = Flask(__name__)

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_USE_TLS = False  
MAIL_USE_SSL = True 


mail = Mail(app_mail)