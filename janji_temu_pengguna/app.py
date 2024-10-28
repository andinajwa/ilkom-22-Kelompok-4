from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Konfigurasi koneksi database
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        database='healthcare_appointments',
        user='root',  # sesuaikan jika Anda menggunakan user lain
        password=''    # sesuaikan dengan password Anda
    )

# Endpoint untuk mencari dokter
@app.route('/doctors', methods=['GET'])
def get_doctors():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM doctors WHERE availability = TRUE")
    doctors = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(doctors)

# Endpoint untuk membuat janji temu
@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO appointments (user_name, doctor_id, appointment_time) VALUES (%s, %s, %s)", 
                   (data['user_name'], data['doctor_id'], data['appointment_time']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Appointment created successfully!"}), 201

# Endpoint untuk melihat janji temu
@app.route('/appointments/<user_name>', methods=['GET'])
def get_appointments(user_name):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM appointments WHERE user_name = %s", (user_name,))
    appointments = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(appointments)

# Endpoint untuk mengelola janji temu
@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM appointments WHERE id = %s", (appointment_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Appointment deleted successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
