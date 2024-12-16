from configs.db_connection import create_connection
import logging
from datetime import timedelta, datetime

# setup logging
logging.basicConfig(filename='attendance_leave.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# function to format time (timedelta or datetime)
def format_time(time_value):
    if isinstance(time_value, timedelta):
        total_seconds = int(time_value.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f"{hours:02}:{minutes:02}"
    elif time_value:
        return time_value.strftime("%H:%M")
    else:
        return "N/A"

# function to format date
def format_date(date_value):
    if date_value:
        return date_value.strftime("%Y-%m-%d")
    else:
        return "N/A"

# function to view attendance records
def view_attendance():
    print("\nFetching attendance records...")
    
    try:
        connection = create_connection()
        cursor = connection.cursor()
        
        query = """
        SELECT a.attendance_id, e.name, a.attendance_date, a.check_in, a.check_out
        FROM attendances a
        JOIN employees e ON a.employee_id = e.id
        ORDER BY a.attendance_date DESC;
        """
        cursor.execute(query)
        records = cursor.fetchall()
        
        if records:
            print("\nAttendance Records:")
            print("=" * 80)
            print(f"{'ID':<5} {'Name':<20} {'Date':<12} {'Check-in':<8} {'Check-out':<8}")
            print("-" * 80)
            for record in records:
                check_in = format_time(record[3])  # Memformat waktu check-in
                check_out = format_time(record[4])  # Memformat waktu check-out
                attendance_date = format_date(record[2])  # Memformat tanggal
                print(f"{record[0]:<5} {record[1]:<20} {attendance_date:<12} {check_in:<8} {check_out:<8}")
            print("=" * 80)
        else:
            print("\nNo attendance records found.")
        
    except Exception as e:
        logging.error(f"Error fetching attendance records: {e}")
        print(f"Error: {e}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


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
            attendance_date = datetime.strptime(attendance_date_input, "%Y-%m-%d").date()
        except ValueError:
            print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
            return
    else:
        attendance_date = datetime.today().date()

    check_in_input = input("Enter Check-in Time (HH:MM) [Leave blank for current time]: ").strip()
    if check_in_input:
        try:
            check_in = datetime.strptime(check_in_input, "%H:%M").time()
        except ValueError:
            print("⚠️ Invalid time format. Please use HH:MM.")
            return
    else:
        check_in = datetime.now().time().replace(second=0, microsecond=0)

    check_out_input = input("Enter Check-out Time (HH:MM) [Leave blank if not yet checked out]: ").strip()
    if check_out_input:
        try:
            check_out = datetime.strptime(check_out_input, "%H:%M").time()
        except ValueError:
            print("⚠️ Invalid time format. Please use HH:MM.")
            return
    else:
        check_out = None

    try:
        connection = create_connection()
        cursor = connection.cursor()
        
        # Check if employee exists
        cursor.execute("SELECT name FROM employees WHERE id = %s", (employee_id,))
        employee = cursor.fetchone()
        if not employee:
            print(f"⚠️ No employee found with ID: {employee_id}")
            return
        
        # insert attendance record
        query = """
        INSERT INTO attendances (employee_id, attendance_date, check_in, check_out)
        VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (employee_id, attendance_date, check_in, check_out))
        connection.commit()
        
        print(f"\n✅ Attendance recorded successfully for {employee[0]} on {attendance_date}!")
        logging.info(f"Recorded attendance for Employee ID {employee_id} on {attendance_date}.")
    
    except Exception as e:
        logging.error(f"Error recording attendance: {e}")
        print(f"\n⚠️ Error recording attendance: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
# function to request leave
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
        start_date = datetime.strptime(start_date_input, "%Y-%m-%d").date()
    except ValueError:
        print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
        return

    end_date_input = input("Enter End Date (YYYY-MM-DD): ").strip()
    try:
        end_date = datetime.strptime(end_date_input, "%Y-%m-%d").date()
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

    try:
        connection = create_connection()
        cursor = connection.cursor()
        
        # Check if employee exists
        cursor.execute("SELECT name FROM employees WHERE id = %s", (employee_id,))
        employee = cursor.fetchone()
        if not employee:
            print(f"⚠️ No employee found with ID: {employee_id}")
            return
        
        # Insert leave request
        query = """
        INSERT INTO leave_request (employee_id, leave_type, start_date, end_date, reason)
        VALUES (%s, %s, %s, %s, %s);
        """
        cursor.execute(query, (employee_id, leave_type, start_date, end_date, reason))
        connection.commit()
        
        print(f"\n✅ Leave request submitted successfully for {employee[0]} from {start_date} to {end_date}!")
        logging.info(f"Leave request submitted for Employee ID {employee_id}: {leave_type} from {start_date} to {end_date}.")
    
    except Exception as e:
        logging.error(f"Error submitting leave request: {e}")
        print(f"\n⚠️ Error submitting leave request: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to view leave requests
def view_leave_requests():
    print("\nFetching leave requests...")

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
        SELECT lr.leave_request_id, e.name, lr.leave_type, lr.start_date, lr.end_date, lr.reason, lr.applied_on
        FROM leave_request lr
        JOIN employees e ON lr.employee_id = e.id
        ORDER BY lr.applied_on DESC;
        """
        cursor.execute(query)
        requests = cursor.fetchall()

        if requests:
            print("\nLeave Requests:")
            print("=" * 100)
            print(f"{'ID':<5} {'Name':<20} {'Type':<15} {'Start Date':<12} {'End Date':<12} {'Status':<10} {'Applied On':<20}")
            print("-" * 100)
            for req in requests:
                applied_on = req[6].strftime("%Y-%m-%d") if req[6] else "N/A"  # Memformat applied_on, jika None ganti dengan 'N/A'
                start_date = format_date(req[3])  # Format tanggal mulai
                end_date = format_date(req[4])  # Format tanggal selesai
                print(f"{req[0]:<5} {req[1]:<20} {req[2]:<15} {start_date:<12} {end_date:<12} {req[5]:<10} {applied_on:<20}")
            print("=" * 100)
        else:
            print("\nNo leave requests found.")

    except Exception as e:
        logging.error(f"Error fetching leave requests: {e}")
        print(f"\n⚠️ Error fetching leave requests: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

