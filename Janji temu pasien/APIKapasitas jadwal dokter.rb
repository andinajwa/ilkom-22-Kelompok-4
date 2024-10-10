# Update kapasitas dokter
@app.route('/doctors/<int:id>/capacity', methods=['PUT'])
def update_capacity(id):
    data = request.get_json()
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE doctors SET capacity=%s WHERE id=%s", (data['capacity'], id))
    mysql.connection.commit()
    return jsonify({'message': 'Doctor capacity updated successfully'})
