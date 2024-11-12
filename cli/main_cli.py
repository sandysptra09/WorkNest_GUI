from employee_data_management_menu import manage_employee_data

def display_dashboard():
    while True:
        print("\n=== WorkNest Management Dashboard ===")
        print("1. Manajemen Data Karyawan")
        print("2. Pelacakan Kehadiran dan Cuti")
        print("3. Layanan Mandiri Karyawan")
        print("4. Pelaporan dan Analisis")
        print("5. Keamanan Berbasis Peran dan Kontrol Akses")
        print("6. Keluar dari Dashboard")
        
        choice = input("Pilih fitur (1-6): ")

        if choice == '1':
            manage_employee_data()
        elif choice == '2':
            print("Fitur Pelacakan Kehadiran dan Cuti - (Placeholder)")
        elif choice == '3':
            print("Fitur Layanan Mandiri Karyawan - (Placeholder)")
        elif choice == '4':
            print("Fitur Pelaporan dan Analisis - (Placeholder)")
        elif choice == '5':
            print("Fitur Keamanan Berbasis Peran dan Kontrol Akses - (Placeholder)")
        elif choice == '6':
            print("Keluar dari dashboard...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    display_dashboard()