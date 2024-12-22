import os
import json

DB_JSON = '../configs/worknest.json'

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
