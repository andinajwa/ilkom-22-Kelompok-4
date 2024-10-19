import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/doctor_service_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False