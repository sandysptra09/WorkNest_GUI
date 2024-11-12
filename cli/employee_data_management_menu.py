from controllers.employee.employee_data_management import (
    add_employee,
    view_employee,
    update_employee,
    delete_employee
)

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
            name = input("Masukkan nama karyawan: ")
            position = input("Masukkan posisi karyawan: ")
            add_employee(name, position)
        elif choice == '2':
            employee_id = input("Masukkan ID karyawan: ")
            view_employee(employee_id)
        elif choice == '3':
            employee_id = input("Masukkan ID karyawan: ")
            name = input("Masukkan nama baru (atau kosong untuk tidak mengubah): ")
            position = input("Masukkan posisi baru (atau kosong untuk tidak mengubah): ")
            update_employee(employee_id, name if name else None, position if position else None)
        elif choice == '4':
            employee_id = input("Masukkan ID karyawan: ")
            delete_employee(employee_id)
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")