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

def view_profile(user):
    print("\n--- 📝 View Profile ---")
    for key, value in user.items():
        print(f"{key.capitalize():<15}: {value}")

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


def record_attendance(user):
    print("\n--- 📝 Record Attendance ---")
    data = read_json_db()
    attendances = data['attendances']

    attendance_date = input("Enter Attendance Date (YYYY-MM-DD) [Leave blank for today]: ").strip()
    if not attendance_date:
        attendance_date = datetime.today().strftime("%Y-%m-%d")

    check_in = input("Enter Check-in Time (HH:MM) [Leave blank for current time]: ").strip()
    if not check_in:
        check_in = datetime.now().strftime("%H:%M")

    check_out = input("Enter Check-out Time (HH:MM) [Leave blank if not yet checked out]: ").strip()

    new_record = {
        "attendance_id": len(attendances) + 1,
        "employee_id": user['id'],
        "attendance_date": attendance_date,
        "check_in": check_in,
        "check_out": check_out if check_out else None
    }
    attendances.append(new_record)
    data['attendances'] = attendances
    save_data(data)
    print("\n✅ Attendance recorded successfully.")

            
def submit_leave_request(user):
    print("\n--- 📅 Submit Leave Request ---")
    data = read_json_db()
    leave_requests = data['leave_requests']

    leave_type = input("Enter Leave Type (e.g., Sick, Vacation): ").strip()
    start_date = input("Enter Start Date (YYYY-MM-DD): ").strip()
    end_date = input("Enter End Date (YYYY-MM-DD): ").strip()
    reason = input("Enter Leave Reason: ").strip()

    if not leave_type or not start_date or not end_date or not reason:
        print("⚠️ All fields are required.")
        return

    new_request = {
        "leave_request_id": len(leave_requests) + 1,
        "employee_id": user['id'],
        "leave_type": leave_type,
        "start_date": start_date,
        "end_date": end_date,
        "reason": reason,
        "applied_on": datetime.today().strftime("%Y-%m-%d"),
        "status": "Pending"
    }
    leave_requests.append(new_request)
    data['leave_requests'] = leave_requests
    save_data(data)
    print("\n✅ Leave request submitted successfully.")
            

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


