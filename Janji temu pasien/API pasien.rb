# Tambah pasien baru
@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO patients (name, contact, email) VALUES (%s, %s, %s)", 
                   (data['name'], data['contact'], data['email']))
    mysql.connection.commit()
    return jsonify({'message': 'Patient added successfully'}), 201

# Lihat daftar pasien
@app.route('/patients', methods=['GET'])
def get_patients():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    return jsonify(patients)

# Update pasien
@app.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    data = request.get_json()
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE patients SET name=%s, contact=%s, email=%s WHERE id=%s", 
                   (data['name'], data['contact'], data['email'], id))
    mysql.connection.commit()
    return jsonify({'message': 'Patient updated successfully'})

# Hapus pasien
@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM patients WHERE id=%s", (id,))
    mysql.connection.commit()
    return jsonify({'message': 'Patient deleted successfully'})
