from flask import Flask
from models import db
from config import Config
from routes import init_routes

# Inisialisasi Aplikasi Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inisialisasi Database
db.init_app(app)

# Inisialisasi Routes
init_routes(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Membuat tabel jika belum ada
    app.run(debug=True)
