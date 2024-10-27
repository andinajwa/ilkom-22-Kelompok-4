import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Ganti dengan password MySQL Anda
        database="healthcare_db"
    )
