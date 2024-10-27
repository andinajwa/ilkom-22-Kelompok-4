from flask import Blueprint, jsonify, request
import models

routes = Blueprint('routes', __name__)

@routes.route('/doctor', methods=['POST'])
def create_doctor():
    data = request.json
    models.create_doctor(data)
    return jsonify({"message": "Profil dokter berhasil dibuat"}), 201

@routes.route('/doctor/<int:id>', methods=['GET'])
def get_doctor(id):
    doctor = models.get_doctor(id)
    if doctor:
        return jsonify({"id": doctor[0], "name": doctor[1], "specialty": doctor[2], "contact": doctor[3]})
    else:
        return jsonify({"message": "Dokter tidak ditemukan"}), 404   

@routes.route('/appointment', methods=['POST'])
def create_appointment():
    data = request.json
    models.create_appointment(data)
    return jsonify({"message": "Janji temu berhasil dibuat"}), 201

@routes.route('/appointments/<int:doctor_id>', methods=['GET'])
def get_appointments(doctor_id):
    appointments = models.get_appointments(doctor_id)
    result = [{"appointment_id": a[0], "patient_id": a[2], "date": a[3], "time": a[4]} for a in appointments]
    return jsonify(result)

@routes.route('/medical_record', methods=['POST'])
def create_medical_record():
    data = request.json
    models.create_medical_record(data)
    models.update_treatment_summary(data['patient_id'])  # Perbarui ringkasan perawatan setelah menambah rekam medis
    return jsonify({"message": "Rekam medis berhasil ditambahkan"}), 201

@routes.route('/patient/<int:patient_id>/summary', methods=['GET'])
def get_patient_treatment_summary(patient_id):
    summary = models.get_patient_treatment_summary(patient_id)
    if summary:
        return jsonify({"treatment_summary": summary})
    else:
        return jsonify({"message": "Laporan perawatan tidak ditemukan"}), 404

