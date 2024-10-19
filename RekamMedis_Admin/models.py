from app import db

# Model untuk data pasien
class Pasien(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(200))
    tanggal_lahir = db.Column(db.Date)

# Model untuk rekam medis
class RekamMedis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pasien_id = db.Column(db.Integer, db.ForeignKey('pasien.id'), nullable=False)
    diagnosis = db.Column(db.String(200), nullable=False)
    tindakan = db.Column(db.String(200), nullable=False)
    tanggal = db.Column(db.Date, nullable=False)
    pasien = db.relationship('Pasien', backref=db.backref('rekam_medis', lazy=True))

# Model untuk manajemen hasil lab
class HasilLab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rekam_medis_id = db.Column(db.Integer, db.ForeignKey('rekam_medis.id'), nullable=False)
    hasil = db.Column(db.String(200), nullable=False)
    rekam_medis = db.relationship('RekamMedis', backref=db.backref('hasil_lab', lazy=True))

# Model untuk manajemen resep dan pengobatan
class ResepPengobatan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rekam_medis_id = db.Column(db.Integer, db.ForeignKey('rekam_medis.id'), nullable=False)
    resep = db.Column(db.String(200), nullable=False)
    rekam_medis = db.relationship('RekamMedis', backref=db.backref('resep_pengobatan', lazy=True))

db.create_all()
