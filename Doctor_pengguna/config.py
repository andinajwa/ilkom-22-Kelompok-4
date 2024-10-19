class Config:
    # Konfigurasi koneksi ke MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/healthcare_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
