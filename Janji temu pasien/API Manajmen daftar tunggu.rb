# Tambah ke daftar tunggu
@app.route('/waitlist', methods=['POST'])
def add_to_waitlist():
    data = request.get_json()
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO waitlist (patient_id, doctor_id, wait_time) VALUES (%s, %s, %s)", 
                   (data['patient_id'], data['doctor_id'], data['wait_time']))
    mysql.connection.commit()
    return jsonify({'message': 'Added to waitlist successfully'}), 201

# Lihat daftar tunggu
@app.route('/waitlist', methods=['GET'])
def get_waitlist():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM waitlist")
    waitlist = cursor.fetchall()
    return jsonify(waitlist)
