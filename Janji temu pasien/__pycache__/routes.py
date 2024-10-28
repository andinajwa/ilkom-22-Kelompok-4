from flask import request, jsonify
from config import app, db
from models import User, Appointment, MedicalRecord, Consultation

# Endpoint untuk daftar pengguna baru
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(name=data['name'], email=data['email'], password=data['password'], phone=data['phone'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})

# Endpoint untuk login pengguna
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email'], password=data['password']).first()
    if user:
        return jsonify({"message": "Login successful", "user_id": user.id})
    return jsonify({"message": "Invalid credentials"}), 401

# Endpoint untuk membuat janji temu
@app.route('/appointment', methods=['POST'])
def create_appointment():
    data = request.json
    new_appointment = Appointment(
        user_id=data['user_id'], doctor_id=data['doctor_id'], 
        appointment_date=data['appointment_date'], status="Pending"
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({"message": "Appointment created successfully!"})

# Endpoint untuk mendapatkan rekam medis
@app.route('/medical_records/<int:user_id>', methods=['GET'])
def get_medical_records(user_id):
    records = MedicalRecord.query.filter_by(user_id=user_id).all()
    return jsonify([{"description": rec.description, "created_at": rec.created_at} for rec in records])

# Endpoint untuk konsultasi
@app.route('/consultation', methods=['POST'])
def create_consultation():
    data = request.json
    new_consultation = Consultation(
        user_id=data['user_id'], doctor_id=data['doctor_id'], 
        complaint=data['complaint'], consultation_date=data['consultation_date']
    )
    db.session.add(new_consultation)
    db.session.commit()
    return jsonify({"message": "Consultation created successfully!"})
