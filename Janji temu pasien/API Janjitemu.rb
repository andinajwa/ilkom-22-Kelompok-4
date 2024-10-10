# Tambah janji temu
@app.route('/appointments', methods=['POST'])
def add_appointment():
    data = request.get_json()
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO appointments (patient_id, doctor_id, appointment_time, status) VALUES (%s, %s, %s, %s)", 
                   (data['patient_id'], data['doctor_id'], data['appointment_time'], 'pending'))
    mysql.connection.commit()
    return jsonify({'message': 'Appointment added successfully'}), 201

# Lihat daftar janji temu
@app.route('/appointments', methods=['GET'])
def get_appointments():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM appointments")
    appointments = cursor.fetchall()
    return jsonify(appointments)

# Konfirmasi janji temu
@app.route('/appointments/<int:id>/confirm', methods=['PUT'])
def confirm_appointment(id):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE appointments SET status=%s WHERE id=%s", ('confirmed', id))
    mysql.connection.commit()
    return jsonify({'message': 'Appointment confirmed successfully'})

# Hapus janji temu
@app.route('/appointments/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM appointments WHERE id=%s", (id,))
    mysql.connection.commit()
    return jsonify({'message': 'Appointment deleted successfully'})
