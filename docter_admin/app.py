from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Konfigurasi Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/doctor_service_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)

# Model Database
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization_id = db.Column(db.Integer, db.ForeignKey('specialization.id'))

class Specialization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    doctors = db.relationship('Doctor', backref='specialization', lazy=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_name = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text, nullable=False)

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    diagnosis = db.Column(db.Text, nullable=False)
    treatment = db.Column(db.Text, nullable=False)
    consultation_id = db.Column(db.Integer, db.ForeignKey('consultation.id'))

# Resource untuk mengelola dokter
class DoctorResource(Resource):
    def get(self):
        doctors = Doctor.query.all()
        return jsonify([{'id': d.id, 'name': d.name, 'specialization': d.specialization.name} for d in doctors])

    def post(self):
        data = request.json
        doctor = Doctor(name=data['name'], specialization_id=data['specialization_id'])
        db.session.add(doctor)
        db.session.commit()
        return jsonify({'message': 'Doctor added successfully'})

# Resource untuk mengelola spesialisasi
class SpecializationResource(Resource):
    def get(self):
        specializations = Specialization.query.all()
        return jsonify([{'id': s.id, 'name': s.name} for s in specializations])

    def post(self):
        data = request.json
        specialization = Specialization(name=data['name'])
        db.session.add(specialization)
        db.session.commit()
        return jsonify({'message': 'Specialization added successfully'})

# Resource untuk mengelola janji temu
class AppointmentResource(Resource):
    def get(self):
        appointments = Appointment.query.all()
        return jsonify([{'id': a.id, 'doctor': a.doctor.name, 'patient_name': a.patient_name, 'date': a.date} for a in appointments])

    def post(self):
        data = request.json
        appointment = Appointment(doctor_id=data['doctor_id'], patient_name=data['patient_name'], date=datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S'))
        db.session.add(appointment)
        db.session.commit()
        return jsonify({'message': 'Appointment added successfully'})

# Resource untuk mengelola konsultasi
class ConsultationResource(Resource):
    def get(self):
        consultations = Consultation.query.all()
        return jsonify([{'id': c.id, 'doctor': c.doctor.name, 'patient_name': c.patient_name, 'details': c.details} for c in consultations])

    def post(self):
        data = request.json
        consultation = Consultation(doctor_id=data['doctor_id'], patient_name=data['patient_name'], details=data['details'])
        db.session.add(consultation)
        db.session.commit()
        return jsonify({'message': 'Consultation added successfully'})

# Resource untuk mengelola rekam medis
class MedicalRecordResource(Resource):
    def get(self):
        records = MedicalRecord.query.all()
        return jsonify([{'id': r.id, 'patient_name': r.patient_name, 'diagnosis': r.diagnosis, 'treatment': r.treatment} for r in records])

    def post(self):
        data = request.json
        record = MedicalRecord(patient_name=data['patient_name'], diagnosis=data['diagnosis'], treatment=data['treatment'], consultation_id=data['consultation_id'])
        db.session.add(record)
        db.session.commit()
        return jsonify({'message': 'Medical record added successfully'})

# Mendaftarkan routes
api.add_resource(DoctorResource, '/doctors')
api.add_resource(SpecializationResource, '/specializations')
api.add_resource(AppointmentResource, '/appointments')
api.add_resource(ConsultationResource, '/consultations')
api.add_resource(MedicalRecordResource, '/medicalrecords')

if __name__ == '__main__':
    app.run(debug=True)