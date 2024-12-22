import os
import json

DB_JSON = 'configs/worknest.json'

def read_json_db():
    if not os.path.exists(DB_JSON):
        print("File worknest.json tidak ditemukan!")
        return {
            'employees': [],
            'admins': [],
            'attendances': [],
            'leave_requests': [],
            'notifications': [],
        }
    
    try:
        with open(DB_JSON, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file JSON: {e}")
        return {
            'employees': [],
            'admins': [],
            'attendances': [],
            'leave_requests': [],
            'notifications': [],
        }
        
def save_data(data):
    try:
        with open(DB_JSON, 'w') as file:
            json.dump(data, file, indent=4)
        # print("Data berhasil disimpan ke worknest.json")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data ke file JSON: {e}")