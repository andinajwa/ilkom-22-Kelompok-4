from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi database MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'appointment_db'

mysql = MySQL(app)

@app.route('/')
def home():
    return "Appointment Microservice API"

if __name__ == "__main__":
    app.run(debug=True)
