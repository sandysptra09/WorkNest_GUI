import json
from getpass import getpass
from utils.utils import read_json_db

def login():
    data = read_json_db()  # Menggunakan fungsi read_json_db untuk memuat data
    print("Data yang dimuat:", data)  # Tambahkan debug
    try:
        print("\n" + "=" * 60)
        print("🔐 Login to WorkNest")
        print("=" * 60)
        
        email = input("📧  Email: ").strip()
        password = getpass(" Password: ").strip()
        
        # Menemukan pengguna berdasarkan email
        user = None
        # Cek di employees
        for emp in data['employees']:
            if emp['email'] == email:
                user = emp
                break
        # Cek di admins jika tidak ditemukan di employees
        if not user:
            for admin in data['admins']:
                if admin['email'] == email:
                    user = admin
                    break
        
        if user:
            # Verifikasi password tanpa hash
            if password == user['password']:
                return user  
            else:
                print("\n❌ Password salah. Coba lagi.")
        else:
            print("\n❌ Pengguna tidak ditemukan. Pastikan email yang Anda masukkan benar.")
    
    except Exception as e:
        print(f'\n⚠️ Terjadi kesalahan saat login: {e}')
        
    # Login gagal
    return None

