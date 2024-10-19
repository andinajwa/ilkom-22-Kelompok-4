import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfigurasi Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/service_pasien'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
