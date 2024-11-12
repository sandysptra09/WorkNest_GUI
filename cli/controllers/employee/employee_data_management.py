
def add_employee(name, position):
    # Implementasi untuk menambahkan karyawan
    print(f"Menambahkan karyawan: {name} dengan posisi: {position}")

def view_employee(employee_id):
    # Implementasi untuk melihat data karyawan
    print(f"Melihat data karyawan dengan ID: {employee_id}")

def update_employee(employee_id, name=None, position=None):
    # Implementasi untuk memperbarui data karyawan
    print(f"Memperbarui data karyawan ID: {employee_id}")
    if name:
        print(f"Nama baru: {name}")
    if position:
        print(f"Posisi baru: {position}")

def delete_employee(employee_id):
    # Implementasi untuk menghapus karyawan
    print(f"Menghapus karyawan dengan ID: {employee_id}")
