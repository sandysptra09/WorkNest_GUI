def add_employee(name, position):
    print(f"Menambahkan karyawan: {name} dengan posisi: {position}")
    
def view_employee(employee_id):
    print(f'Melihat data karyawan dengan ID: {employee_id}')

def update_employee(employee_id, name=None, position=None):
    print(f'Memperbarui data karyawan ID: {employee_id}')
    if name:
        print(f'Nama baru: {name}')
    if position:
        print(f'Posisi baru: {position}')

def delete_employee(employee_id):
    print(f'Menghapus karyawan dengan ID: {employee_id}')
    