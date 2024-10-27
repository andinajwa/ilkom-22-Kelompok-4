from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfigurasi Database MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/rekam_medis'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
