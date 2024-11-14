# Data dummy karyawan
employees = {
    1: {"name": "John Doe", "attendance": ["Present", "Absent", "Present"], "leave_requests": [], "performance": "Good"},
    2: {"name": "Jane Smith", "attendance": ["Present", "Present", "Present"], "leave_requests": [], "performance": "Excellent"},
    3: {"name": "Alice Johnson", "attendance": ["Absent", "Present", "Present"], "leave_requests": [], "performance": "Satisfactory"}
}

# Fungsi untuk mengakses profil karyawan berdasarkan nama
def get_employee_id_by_name(name):
    for id, data in employees.items():
        if data["name"].lower() == name.lower():
            return id
    return None

def get_profile(employee_id):
    employee = employees.get(employee_id)
    if employee:
        return employee
    else:
        return {"error": "Employee not found"}

def get_attendance(employee_id):
    employee = employees.get(employee_id)
    if employee:
        return {"attendance": employee['attendance']}
    else:
        return {"error": "Employee not found"}

def leave_request(employee_id, leave_date, reason):
    employee = employees.get(employee_id)
    if not employee:
        return {"error": "Employee not found"}

    if not leave_date or not reason:
        return {"error": "Date and reason are required"}

    employee['leave_requests'].append({"date": leave_date, "reason": reason})
    return {"message": "Leave request submitted successfully"}

def get_performance(employee_id):
    employee = employees.get(employee_id)
    if employee:
        return {"performance": employee['performance']}
    else:
        return {"error": "Employee not found"}

# Input nama karyawan
employee_name = input("Masukkan nama karyawan: ")
employee_id = get_employee_id_by_name(employee_name)

if employee_id:
    print("Profil:", get_profile(employee_id))
    print("Kehadiran:", get_attendance(employee_id))
    leave_date = input("Masukkan tanggal cuti (YYYY-MM-DD): ")
    leave_reason = input("Masukkan alasan cuti: ")
    print(leave_request(employee_id, leave_date, leave_reason))
    print("Kinerja:", get_performance(employee_id))
else:
    print("Karyawan tidak ditemukan.")
