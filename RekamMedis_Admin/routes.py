from flask import request, jsonify
from app import app, db
from models import Pasien, RekamMedis, HasilLab, ResepPengobatan

# CRUD untuk Pasien
@app.route('/pasien', methods=['POST'])
def create_pasien():
    data = request.json
    new_pasien = Pasien(nama=data['nama'], alamat=data['alamat'], tanggal_lahir=data['tanggal_lahir'])
    db.session.add(new_pasien)
    db.session.commit()
    return jsonify({"message": "Pasien created successfully!"})

@app.route('/pasien', methods=['GET'])
def get_pasien():
    pasien = Pasien.query.all()
    result = []
    for p in pasien:
        result.append({
            'id': p.id,
            'nama': p.nama,
            'alamat': p.alamat,
            'tanggal_lahir': p.tanggal_lahir
        })
    return jsonify(result)

# CRUD untuk Rekam Medis
@app.route('/rekam-medis', methods=['POST'])
def create_rekam_medis():
    data = request.json
    new_rekam_medis = RekamMedis(pasien_id=data['pasien_id'], diagnosis=data['diagnosis'], tindakan=data['tindakan'], tanggal=data['tanggal'])
    db.session.add(new_rekam_medis)
    db.session.commit()
    return jsonify({"message": "Rekam medis created successfully!"})

@app.route('/rekam-medis', methods=['GET'])
def get_rekam_medis():
    rekam_medis = RekamMedis.query.all()
    result = []
    for rm in rekam_medis:
        result.append({
            'id': rm.id,
            'pasien_id': rm.pasien_id,
            'diagnosis': rm.diagnosis,
            'tindakan': rm.tindakan,
            'tanggal': rm.tanggal
        })
    return jsonify(result)

# CRUD untuk Hasil Lab
@app.route('/hasil-lab', methods=['POST'])
def create_hasil_lab():
    data = request.json
    new_hasil_lab = HasilLab(rekam_medis_id=data['rekam_medis_id'], hasil=data['hasil'])
    db.session.add(new_hasil_lab)
    db.session.commit()
    return jsonify({"message": "Hasil lab created successfully!"})

@app.route('/hasil-lab', methods=['GET'])
def get_hasil_lab():
    hasil_lab = HasilLab.query.all()
    result = []
    for hl in hasil_lab:
        result.append({
            'id': hl.id,
            'rekam_medis_id': hl.rekam_medis_id,
            'hasil': hl.hasil
        })
    return jsonify(result)

# CRUD untuk Resep Pengobatan
@app.route('/resep-pengobatan', methods=['POST'])
def create_resep_pengobatan():
    data = request.json
    new_resep_pengobatan = ResepPengobatan(rekam_medis_id=data['rekam_medis_id'], resep=data['resep'])
    db.session.add(new_resep_pengobatan)
    db.session.commit()
    return jsonify({"message": "Resep pengobatan created successfully!"})

@app.route('/resep-pengobatan', methods=['GET'])
def get_resep_pengobatan():
    resep_pengobatan = ResepPengobatan.query.all()
    result = []
    for rp in resep_pengobatan:
        result.append({
            'id': rp.id,
            'rekam_medis_id': rp.rekam_medis_id,
            'resep': rp.resep
        })
    return jsonify(result)
