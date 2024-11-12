print('inialization main cli')
def display_dashboard():
    while True:
        print("\n=== WorkNest Management Dashboard ===")
        print("1. Manajemen Data Karyawan")
        print("2. Pelacakan Kehadiran dan Cuti")
        print("3. Layanan Mandiri Karyawan")
        print("4. Pelaporan dan Analisis")
        print("5. Keamanan Berbasis Peran dan Kontrol Akses")
        print("6. Exit")
        
        choice = input("Pilih fitur (1-6): ")

        if choice == '1':
            manage_employee_data()
        elif choice == '2':
            track_attendance_and_leave()
        elif choice == '3':
            employee_self_service()
        elif choice == '4':
            reporting_and_analytics()
        elif choice == '5':
            role_based_security_and_access_control()
        elif choice == '6':
            print("Keluar dari dashboard...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def manage_employee_data():
    while True:
        print("\n--- Manajemen Data Karyawan ---")
        print("1. Tambah Karyawan")
        print("2. Lihat Karyawan")
        print("3. Perbarui Karyawan")
        print("4. Hapus Karyawan")
        print("5. Kembali ke Menu Utama")
        
        choice = input("Pilih menu [1-5]: ")

        if choice == '1':
            print("Fitur Tambah Karyawan - (Placeholder)")
           
        elif choice == '2':
            print("Fitur Lihat Karyawan - (Placeholder)")
            
        elif choice == '3':
            print("Fitur Perbarui Karyawan - (Placeholder)")
            
        elif choice == '4':
            print("Fitur Hapus Karyawan - (Placeholder)")
            
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def track_attendance_and_leave():
    print("Fitur Pelacakan Kehadiran dan Cuti - (Placeholder)")
    

def employee_self_service():
    print("Fitur Layanan Mandiri Karyawan - (Placeholder)")
   
def reporting_and_analytics():
    print("Fitur Pelaporan dan Analisis - (Placeholder)")
    
def role_based_security_and_access_control():
    print("Fitur Keamanan Berbasis Peran dan Kontrol Akses - (Placeholder)")
    

if __name__ == "__main__":
    display_dashboard()
