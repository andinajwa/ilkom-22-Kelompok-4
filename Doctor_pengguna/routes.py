from flask import request, jsonify
from models import db, User, Appointment, MedicalRecord, Consultation
from datetime import datetime

def init_routes(app):
    # Route: Tambah User
    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        user = User(
            name=data['name'],
            email=data['email'],
            role=data['role'],
            password=data['password']
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201

    # Route: Buat Janji Temu
    @app.route('/appointments', methods=['POST'])
    def create_appointment():
        data = request.get_json()
        appointment = Appointment(
            doctor_id=data['doctor_id'],
            patient_id=data['patient_id'],
            appointment_date=datetime.strptime(data['appointment_date'], '%Y-%m-%d %H:%M:%S'),
            status='scheduled'
        )
        db.session.add(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment created successfully'}), 201

    # Route: Ambil Rekam Medis
    @app.route('/medical_records/<int:patient_id>', methods=['GET'])
    def get_medical_records(patient_id):
        records = MedicalRecord.query.filter_by(patient_id=patient_id).all()
        return jsonify([{
            'id': record.id,
            'diagnosis': record.diagnosis,
            'treatment': record.treatment,
            'date': record.date
        } for record in records]), 200

    # Route: Buat Konsultasi
    @app.route('/consultations', methods=['POST'])
    def create_consultation():
        data = request.get_json()
        consultation = Consultation(
            patient_id=data['patient_id'],
            doctor_id=data['doctor_id'],
            message=data['message']
        )
        db.session.add(consultation)
        db.session.commit()
        return jsonify({'message': 'Consultation created successfully'}), 201

    # Route: Ambil Laporan Konsultasi
    @app.route('/consultations/<int:doctor_id>', methods=['GET'])
    def get_consultations(doctor_id):
        consultations = Consultation.query.filter_by(doctor_id=doctor_id).all()
        return jsonify([{
            'patient_id': c.patient_id,
            'message': c.message,
            'response': c.response,
            'date': c.consultation_date
        } for c in consultations]), 200
