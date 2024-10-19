from flask import Flask, request, jsonify
from models import db, Pengguna, RekamMedis, HasilLab, Resep
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# API CRUD untuk Pengguna
@app.route('/pengguna', methods=['POST'])
def buat_pengguna():
    data = request.get_json()
    pengguna = Pengguna(nama=data['nama'], email=data['email'], password=data['password'])
    db.session.add(pengguna)
    db.session.commit()
    return jsonify({'message': 'Pengguna berhasil dibuat'}), 201

@app.route('/pengguna/<int:id>', methods=['GET'])
def get_pengguna(id):
    pengguna = Pengguna.query.get_or_404(id)
    return jsonify({'id': pengguna.id, 'nama': pengguna.nama, 'email': pengguna.email})

@app.route('/pengguna/<int:id>', methods=['PUT'])
def update_pengguna(id):
    data = request.get_json()
    pengguna = Pengguna.query.get_or_404(id)
    pengguna.nama = data['nama']
    pengguna.email = data['email']
    pengguna.password = data['password']
    db.session.commit()
    return jsonify({'message': 'Pengguna berhasil diperbarui'})

@app.route('/pengguna/<int:id>', methods=['DELETE'])
def delete_pengguna(id):
    pengguna = Pengguna.query.get_or_404(id)
    db.session.delete(pengguna)
    db.session.commit()
    return jsonify({'message': 'Pengguna berhasil dihapus'})

# API untuk Rekam Medis
@app.route('/rekam_medis', methods=['POST'])
def buat_rekam_medis():
    data = request.get_json()
    rekam_medis = RekamMedis(pengguna_id=data['pengguna_id'], diagnosa=data['diagnosa'])
    db.session.add(rekam_medis)
    db.session.commit()
    return jsonify({'message': 'Rekam medis berhasil dibuat'})

@app.route('/rekam_medis/<int:id>', methods=['GET'])
def get_rekam_medis(id):
    rekam_medis = RekamMedis.query.get_or_404(id)
    return jsonify({'id': rekam_medis.id, 'diagnosa': rekam_medis.diagnosa, 'tanggal': rekam_medis.tanggal})

@app.route('/rekam_medis/<int:id>', methods=['PUT'])
def update_rekam_medis(id):
    data = request.get_json()
    rekam_medis = RekamMedis.query.get_or_404(id)
    rekam_medis.diagnosa = data['diagnosa']
    db.session.commit()
    return jsonify({'message': 'Rekam medis berhasil diperbarui'})

@app.route('/rekam_medis/<int:id>', methods=['DELETE'])
def delete_rekam_medis(id):
    rekam_medis = RekamMedis.query.get_or_404(id)
    db.session.delete(rekam_medis)
    db.session.commit()
    return jsonify({'message': 'Rekam medis berhasil dihapus'})

# API untuk Hasil Lab
@app.route('/hasil_lab', methods=['POST'])
def buat_hasil_lab():
    data = request.get_json()
    hasil_lab = HasilLab(rekam_medis_id=data['rekam_medis_id'], hasil=data['hasil'])
    db.session.add(hasil_lab)
    db.session.commit()
    return jsonify({'message': 'Hasil lab berhasil dibuat'})

@app.route('/hasil_lab/<int:id>', methods=['GET'])
def get_hasil_lab(id):
    hasil_lab = HasilLab.query.get_or_404(id)
    return jsonify({'id': hasil_lab.id, 'hasil': hasil_lab.hasil})

# API untuk Resep
@app.route('/resep', methods=['POST'])
def buat_resep():
    data = request.get_json()
    resep = Resep(rekam_medis_id=data['rekam_medis_id'], obat=data['obat'], dosis=data['dosis'])
    db.session.add(resep)
    db.session.commit()
    return jsonify({'message': 'Resep berhasil dibuat'})

@app.route('/resep/<int:id>', methods=['GET'])
def get_resep(id):
    resep = Resep.query.get_or_404(id)
    return jsonify({'id': resep.id, 'obat': resep.obat, 'dosis': resep.dosis})

if __name__ == '__main__':
    app.run(debug=True)
