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
    
def bubble_sort_by_date(records): # bubble sorting untuk attendance date
    n = len(records)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Konversi tanggal ke objek datetime untuk perbandingan
            date1 = datetime.strptime(records[j]["attendance_date"], "%Y-%m-%d")
            date2 = datetime.strptime(records[j + 1]["attendance_date"], "%Y-%m-%d")
            if date1 > date2:
                # Tukar posisi jika tanggal lebih besar
                records[j], records[j + 1] = records[j + 1], records[j]
    return records

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

        # Sorting attendance records by date
        attendances = bubble_sort_by_date(attendances)
        
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
            print("=" * 100)
            print(f"{'ID':<5} {'Name':<20} {'Date':<20} {'Status':<15} {'Check-in':<14} {'Check-out':<14}")
            print("-" * 100)

            for record in paginated_records:
                employee = next((e for e in employees if e["id"] == record["employee_id"]), None)
                if not employee:
                    # skip if employee data not found
                    continue  

                name = employee.get("name", "Unknown")
                attendance_date = format_date(record.get("attendance_date", ""))
                status = record.get("status", "Unknown")
                check_in = format_time(record.get("check_in", "")) if record.get("check_in") else "N/A"
                check_out = format_time(record.get("check_out", "")) if record.get("check_out") else "N/A"

                print(f"{record['attendance_id']:<5} {name:<20} {attendance_date:<20} {status:<15} {check_in:<14} {check_out:<14}")
            print("=" * 100)

            # pagination navigation
            next_action = input("\nPress 'n' for next page, or any other key to exit: ").strip().lower()
            if next_action == 'n':
                offset += limit
            else:
                break

    except Exception as e:
        print(f"\n⚠️ Error: {e}")

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
        print("=" * 120)
        print(f"{'ID':<5} {'Name':<20} {'Type':<15} {'Start Date':<12} {'End Date':<12} {'Reason':<30} {'Applied On':<15} {'Status':<10}")
        print("-" * 120)

        for req in leave_requests:
            employee = next((e for e in employees if e["id"] == req["employee_id"]), None)
            if not employee:
                continue

            print(
                f"{req['leave_request_id']:<5} "
                f"{employee['name']:<20} "
                f"{req['leave_type']:<15} "
                f"{format_date(req['start_date']):<12} "
                f"{format_date(req['end_date']):<12} "
                f"{req['reason']:<30} "
                f"{format_date(req['applied_on']):<15} "
                f"{req['status']:<10}"
            )
        print("=" * 120)

    except Exception as e:
        print(f"\n⚠️ Error: {e}")


# function to manage leave requests (approve/reject)
def manage_leave_requests(leave_requests):
    try:
        request_id = int(input("Enter Leave Request ID to manage: ").strip())
        leave_request = next((req for req in leave_requests if req['leave_request_id'] == request_id), None)

        if leave_request:
            print(f"\nLeave Request Details:\nType: {leave_request['leave_type']}, Start: {format_date(leave_request['start_date'])}, End: {format_date(leave_request['end_date'])}, Status: {leave_request['status']}")
            decision = input("Approve or Reject? (approve/reject): ").strip().lower()

            if decision in ["approve", "reject"]:
                leave_request['status'] = "Approved" if decision == "approve" else "Rejected"

                data = read_json_db()                
                data['leave_requests'] = leave_requests
                save_data(data)
                
                print(f"\n✅ Leave request has been {leave_request['status'].lower()}.")
            else:
                print("⚠️ Invalid decision. Please choose 'approve' or 'reject'.")
        else:
            print(f"⚠️ No leave request found with ID: {request_id}")
    except ValueError:
        print("⚠️ Invalid input. Please enter a numeric ID.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

