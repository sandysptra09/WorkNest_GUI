import json
import os

# File untuk menyimpan data karyawan
DATA_FILE = './cli/configs/worknest.json'

# Fungsi untuk memuat data karyawan dari file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            return data['employees'], data.get('attendance_records', {})
    return [], {}

# Fungsi untuk menyimpan data karyawan ke file
def save_data(employees, attendance_records):
    data = {
        'employees': employees,
        'attendance_records': attendance_records
    }
    
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)