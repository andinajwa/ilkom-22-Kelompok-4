from config import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    doctor_id = db.Column(db.Integer, nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)

class MedicalRecord(db.Model):
    __tablename__ = 'medical_records'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Consultation(db.Model):
    __tablename__ = 'consultations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    doctor_id = db.Column(db.Integer, nullable=False)
    complaint = db.Column(db.Text, nullable=False)
    consultation_date = db.Column(db.DateTime, nullable=False)
