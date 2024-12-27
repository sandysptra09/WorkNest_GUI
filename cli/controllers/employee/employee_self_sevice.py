import json
from utils.utils import read_json_db, save_data
from datetime import datetime

# function to format date
def format_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%d %B %Y")
    except ValueError:
        return date_str

# function to format time
def format_time(time_str):
    try:
        return datetime.strptime(time_str, "%H:%M").strftime("%I:%M %p")
    except ValueError:
        return time_str

# 
def view_profile(user):
    print("\n--- 📝 View Profile ---")
    for key, value in user.items():
        print(f"{key.capitalize():<15}: {value}")

# function to view attendance records
def view_attendance(user):
    print("\n--- 📅 View Attendance Records ---")
    data = read_json_db()
    attendances = data['attendances']
    user_attendance = [att for att in attendances if att['employee_id'] == user['id']]

    if user_attendance:
        print("\nAttendance Records:\n")
        print(f"{'Date':<20} {'Check-in':<15} {'Check-out':<15}")
        print("-" * 50)
        for record in user_attendance:
            formatted_date = format_date(record['attendance_date'])
            formatted_check_in = format_time(record['check_in'])
            formatted_check_out = format_time(record.get('check_out', "N/A"))
            print(f"{formatted_date:<20} {formatted_check_in:<15} {formatted_check_out:<15}")
    else:
        print("No attendance records found.")

# function to record attendance
def record_attendance(user):
    print("\n--- 📝 Record Attendance ---")

    # Ambil ID karyawan dari user
    employee_id = user.get("id")
    if not employee_id:
        print("⚠️ Unable to determine the employee ID.")
        return

    attendance_date_input = input("Enter Attendance Date (YYYY-MM-DD) [Leave blank for today]: ").strip()
    if attendance_date_input:
        try:
            attendance_date = datetime.strptime(attendance_date_input, "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
            return
    else:
        attendance_date = datetime.today().date().isoformat()

    check_in_input = input("Enter Check-in Time (HH:MM) [Leave blank for current time]: ").strip()
    if check_in_input:
        try:
            check_in = datetime.strptime(check_in_input, "%H:%M").time().isoformat()
        except ValueError:
            print("⚠️ Invalid time format. Please use HH:MM.")
            return
    else:
        check_in = datetime.now().time().replace(second=0, microsecond=0).isoformat()

    check_out_input = input("Enter Check-out Time (HH:MM) [Leave blank if not yet checked out]: ").strip()
    check_out = None
    if check_out_input:
        try:
            check_out = datetime.strptime(check_out_input, "%H:%M").time().isoformat()
        except ValueError:
            print("⚠️ Invalid time format. Please use HH:MM.")
            return

    data = read_json_db()
    employees = data.get("employees", [])
    attendances = data.get("attendances", [])

    employee = next((e for e in employees if e["id"] == employee_id), None)
    if not employee:
        print(f"⚠️ No employee found with ID: {employee_id}")
        return

    # Check for duplicate attendance record
    for att in attendances:
        if att["employee_id"] == employee_id and att["attendance_date"] == attendance_date:
            print(f"⚠️ Attendance for {attendance_date} already exists for this employee.")
            return

    attendance_id = len(attendances) + 1
    new_record = {
        "attendance_id": attendance_id,
        "employee_id": employee_id,
        "attendance_date": attendance_date,
        "check_in": check_in,
        "check_out": check_out
    }
    attendances.append(new_record)
    data["attendances"] = attendances

    save_data(data)
    print(f"\n✅ Attendance recorded successfully for {employee['name']} on {attendance_date}!")

# function to request leave
def request_leave(user):
    print("\n--- 🗒️ Request Leave ---")

    # Ambil employee_id dari user
    employee_id = user.get("id")
    if not employee_id:
        print("⚠️ Unable to determine the employee ID.")
        return

    leave_type = input("Enter Leave Type (e.g., Sick, Vacation): ").strip()
    if not leave_type:
        print("⚠️ Leave Type cannot be empty.")
        return

    start_date_input = input("Enter Start Date (YYYY-MM-DD): ").strip()
    try:
        start_date = datetime.strptime(start_date_input, "%Y-%m-%d").date().isoformat()
    except ValueError:
        print("⚠️ Invalid Start Date format. Please use YYYY-MM-DD.")
        return

    end_date_input = input("Enter End Date (YYYY-MM-DD): ").strip()
    try:
        end_date = datetime.strptime(end_date_input, "%Y-%m-%d").date().isoformat()
    except ValueError:
        print("⚠️ Invalid End Date format. Please use YYYY-MM-DD.")
        return

    if end_date < start_date:
        print("⚠️ End Date cannot be earlier than Start Date.")
        return

    reason = input("Enter Leave Reason: ").strip()
    if not reason:
        print("⚠️ Leave Reason cannot be empty.")
        return

    data = read_json_db()
    employees = data.get("employees", [])
    leave_requests = data.get("leave_requests", [])

    employee = next((e for e in employees if e["id"] == employee_id), None)
    if not employee:
        print(f"⚠️ No employee found with ID: {employee_id}")
        return

    leave_request_id = len(leave_requests) + 1
    new_request = {
        "leave_request_id": leave_request_id,
        "employee_id": employee_id,
        "leave_type": leave_type,
        "start_date": start_date,
        "end_date": end_date,
        "reason": reason,
        "applied_on": datetime.today().isoformat(),
        "status": "Pending"
    }
    leave_requests.append(new_request)
    data["leave_requests"] = leave_requests

    save_data(data)
    print(f"\n✅ Leave request submitted successfully for {employee['name']}!")


# function to view leave requests
def view_leave_status(user):
    print("\n--- 📂 View Leave Status ---")
    data = read_json_db()
    leave_requests = data['leave_requests']
    user_requests = [req for req in leave_requests if req['employee_id'] == user['id']]

    if user_requests:
        print("\nLeave Requests:\n")
        for req in user_requests:
            formatted_start_date = format_date(req['start_date'])
            formatted_end_date = format_date(req['end_date'])
            print(f"Type: {req['leave_type']}, Start: {formatted_start_date}, End: {formatted_end_date}, Reason: {req['reason']}, Status: {req['status']}")
    else:
        print("No leave requests found.")


