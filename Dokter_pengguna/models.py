from config import get_db_connection

# Fungsi untuk menambah dokter baru
def create_doctor(data):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO doctors (name, specialty, contact) VALUES (%s, %s, %s)",
                   (data['name'], data['specialty'], data['contact']))
    db.commit()
    cursor.close()
    db.close()

# Fungsi untuk mendapatkan profil dokter
def get_doctor(id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM doctors WHERE id = %s", (id,))
    doctor = cursor.fetchone()
    cursor.close()
    db.close()
    return doctor

# Fungsi untuk menambah janji temu baru
def create_appointment(data):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO appointments (doctor_id, patient_id, date, time) VALUES (%s, %s, %s, %s)",
                   (data['doctor_id'], data['patient_id'], data['date'], data['time']))
    db.commit()
    cursor.close()
    db.close()

# Fungsi untuk mendapatkan janji temu dokter
def get_appointments(doctor_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM appointments WHERE doctor_id = %s", (doctor_id,))
    appointments = cursor.fetchall()
    cursor.close()
    db.close()
    return appointments

# Fungsi untuk menambah rekam medis
def create_medical_record(data):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO medical_records (patient_id, doctor_id, diagnosis, treatment) VALUES (%s, %s, %s, %s)",
                   (data['patient_id'], data['doctor_id'], data['diagnosis'], data['treatment']))
    db.commit()
    cursor.close()
    db.close()

# Fungsi untuk memperbarui laporan perawatan pasien
def update_treatment_summary(patient_id):
    db = get_db_connection()
    cursor = db.cursor()
    
    # Mengambil ringkasan dari rekam medis pasien
    cursor.execute("""
        SELECT diagnosis, treatment, COUNT(*) as count
        FROM medical_records
        WHERE patient_id = %s
        GROUP BY diagnosis, treatment
    """, (patient_id,))
    records = cursor.fetchall()
    
    # Menyusun laporan perawatan
    summary = ""
    for record in records:
        summary += f"Diagnosis: {record[0]}, Treatment: {record[1]}, Count: {record[2]}\n"
    
    # Memperbarui kolom `treatment_summary` di tabel `patients`
    cursor.execute("""
        UPDATE patients
        SET treatment_summary = %s
        WHERE id = %s
    """, (summary, patient_id))
    
    db.commit()
    cursor.close()
    db.close()

# Fungsi untuk mendapatkan laporan perawatan pasien
def get_patient_treatment_summary(patient_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT treatment_summary FROM patients WHERE id = %s", (patient_id,))
    summary = cursor.fetchone()
    cursor.close()
    db.close()
    return summary[0] if summary else None
