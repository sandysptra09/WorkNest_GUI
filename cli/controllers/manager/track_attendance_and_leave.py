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
        return datetime.strptime(time_str, "%H:%M:%S").strftime("%I:%M %p")
    except ValueError:
        return time_str

# function to view attendance records
def view_attendance():
    print("\nFetching attendance records...")

    try:
        data = read_json_db()
        attendances = data.get("attendances", [])
        employees = data.get("employees", [])

        if not attendances:
            print("\nNo attendance records found.")
            return

        # pagination setup
        limit = 10
        offset = 0

        while True:
            # fetch subset of attendance records
            paginated_records = attendances[offset:offset + limit]

            if not paginated_records:
                print("\nNo more attendance records found.")
                break

            print("\nAttendance Records:")
            print("=" * 80)
            print(f"{'ID':<5} {'Name':<20} {'Date':<20} {'Check-in':<14} {'Check-out':<14}")
            print("-" * 80)

            for record in paginated_records:
                employee = next((e for e in employees if e["id"] == record["employee_id"]), None)
                if not employee:
                    # skip if employee data not found
                    continue  
                
                name = employee.get("name", "Unknown")
                attendance_date = format_date(record.get("attendance_date", ""))
                check_in = format_time(record.get("check_in", ""))
                check_out = format_time(record.get("check_out", ""))

                print(f"{record['attendance_id']:<5} {name:<20} {attendance_date:<20} {check_in:<14} {check_out:<14}")
            print("=" * 80)

            # pagination navigation
            next_action = input("\nPress 'n' for next page, or any other key to exit: ").strip().lower()
            if next_action == 'n':
                offset += limit
            else:
                break

    except Exception as e:
        print(f"\n⚠️ Error: {e}")


# function to record attendance for an employee
def record_attendance():
    print("\n--- 📝 Record Attendance ---")

    try:
        employee_id = int(input("Enter Employee ID: ").strip())
    except ValueError:
        print("⚠️ Invalid Employee ID. It should be a number.")
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

# Function to request leave
def request_leave():
    print("\n--- 🗒️ Request Leave ---")

    try:
        employee_id = int(input("Enter Employee ID: ").strip())
    except ValueError:
        print("⚠️ Invalid Employee ID. It should be a number.")
        return

    leave_type = input("Enter Leave Type (e.g., Sick, Vacation): ").strip()
    if not leave_type:
        print("⚠️ Leave Type cannot be empty.")
        return

    start_date_input = input("Enter Start Date (YYYY-MM-DD): ").strip()
    try:
        start_date = datetime.strptime(start_date_input, "%Y-%m-%d").date().isoformat()
    except ValueError:
        print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
        return

    end_date_input = input("Enter End Date (YYYY-MM-DD): ").strip()
    try:
        end_date = datetime.strptime(end_date_input, "%Y-%m-%d").date().isoformat()
    except ValueError:
        print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
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
        "applied_on": datetime.today().date().isoformat()
    }
    leave_requests.append(new_request)
    data["leave_requests"] = leave_requests

    save_data(data)
    print(f"\n✅ Leave request submitted successfully for {employee['name']} from {start_date} to {end_date}!")


# function to view leave requests
def view_leave_requests():
    print("\nFetching leave requests...")

    try:
        data = read_json_db()
        leave_requests = data.get("leave_requests", [])
        employees = data.get("employees", [])

        if not leave_requests:
            print("\nNo leave requests found.")
            return

        print("\nLeave Requests:")
        print("=" * 100)
        print(f"{'ID':<5} {'Name':<20} {'Type':<15} {'Start Date':<12} {'End Date':<12} {'Reason':<20} {'Applied On':<12}")
        print("-" * 100)

        for req in leave_requests:
            employee = next((e for e in employees if e["id"] == req["employee_id"]), None)
            if not employee:
                continue

            print(f"{req['leave_request_id']:<5} {employee['name']:<20} {req['leave_type']:<15} {format_date(req['start_date']):<12} {format_date(req['end_date']):<12} {req['reason']:<20} {format_date(req['applied_on']):<12}")
        print("=" * 100)

    except Exception as e:
        print(f"\n⚠️ Error: {e}")

