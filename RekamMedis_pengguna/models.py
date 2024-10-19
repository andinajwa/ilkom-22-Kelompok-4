from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Model Pengguna
class Pengguna(db.Model):
    __tablename__ = 'pengguna'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

# Model Rekam Medis
class RekamMedis(db.Model):
    __tablename__ = 'rekam_medis'
    id = db.Column(db.Integer, primary_key=True)
    pengguna_id = db.Column(db.Integer, db.ForeignKey('pengguna.id'), nullable=False)
    diagnosa = db.Column(db.String(200), nullable=False)
    tanggal = db.Column(db.DateTime, default=datetime.utcnow)
    pengguna = db.relationship('Pengguna', backref='rekam_medis')

# Model Hasil Lab
class HasilLab(db.Model):
    __tablename__ = 'hasil_lab'
    id = db.Column(db.Integer, primary_key=True)
    rekam_medis_id = db.Column(db.Integer, db.ForeignKey('rekam_medis.id'), nullable=False)
    hasil = db.Column(db.String(200), nullable=False)
    rekam_medis = db.relationship('RekamMedis', backref='hasil_lab')

# Model Resep
class Resep(db.Model):
    __tablename__ = 'resep'
    id = db.Column(db.Integer, primary_key=True)
    rekam_medis_id = db.Column(db.Integer, db.ForeignKey('rekam_medis.id'), nullable=False)
    obat = db.Column(db.String(100), nullable=False)
    dosis = db.Column(db.String(100), nullable=False)
    rekam_medis = db.relationship('RekamMedis', backref='resep')
