from datetime import datetime, timedelta
import logging
from configs.db_connection import create_connection

def format_time(time_value):
    """Format time for display."""
    if isinstance(time_value, timedelta):
        total_seconds = int(time_value.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f"{hours:02}:{minutes:02}"
    elif time_value:
        return time_value.strftime("%H:%M")
    else:
        return "N/A"

def format_date(date_value):
    """Format date for display."""
    if date_value:
        return date_value.strftime("%Y-%m-%d")
    else:
        return "N/A"

def view_profile(user):
    """View user profile."""
    print("\n--- 📄 View Profile ---")
    print(f"Name            : {user['name']}")
    print(f"NIP             : {user['nip']}")  
    print(f"Gender          : {user['gender']}")
    print(f"Birth Place     : {user['birth_place']}")
    print(f"Birth Date      : {user['birth_date']}")
    print(f"Phone           : {user['phone']}")
    print(f"Religion        : {user['religion']}")
    print(f"Marital Status  : {user['marital_status']}")
    print(f"Address         : {user['address']}")
    print(f"Email           : {user['email']}")
    print(f"Role            : {user['role']}")

def view_attendance(user):
    """View attendance records for a specific user."""
    print("\n--- 🗓️ View Attendance Records ---")
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
        SELECT attendance_date, check_in, check_out
        FROM attendances
        WHERE employee_id = %s
        ORDER BY attendance_date DESC;
        """
        cursor.execute(query, (user['id'],))
        records = cursor.fetchall()

        if records:
            print(f"\nAttendance Records for {user['name']}:\n")
            print("=" * 50)
            print(f"{'Date':<12} {'Check-in':<8} {'Check-out':<8}")
            print("-" * 50)
            for record in records:
                attendance_date = format_date(record[0])
                check_in = format_time(record[1])
                check_out = format_time(record[2])
                print(f"{attendance_date:<12} {check_in:<8} {check_out:<8}")
            print("=" * 50)
        else:
            print(f"\nNo attendance records found for {user['name']}.")

    except Exception as e:
        logging.error(f"Error fetching attendance records: {e}")
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def record_attendance(user):
    """Record attendance for an employee."""
    print("\n--- 📝 Record Attendance ---")

    # Ambil employee_id langsung dari user yang sedang login
    employee_id = user['id']
    print(f"Recording attendance for Employee ID: {employee_id} ({user['name']})")

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

        query = """
        INSERT INTO attendances (employee_id, attendance_date, check_in, check_out)
        VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (employee_id, attendance_date, check_in, check_out))
        connection.commit()

        print(f"\n✅ Attendance recorded successfully for {user['name']} on {attendance_date}!")
        logging.info(f"Recorded attendance for Employee ID {employee_id} on {attendance_date}.")

    except Exception as e:
        logging.error(f"Error recording attendance: {e}")
        print(f"\n⚠️ Error recording attendance: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
def submit_leave_request(user):
    print("\n--- 🖒 Request Leave ---")

    # Employee ID langsung diambil dari user yang login
    employee_id = user['id']
    print(f"Submitting leave request for Employee ID: {employee_id} ({user['name']})")

    leave_type = input("Enter Leave Type (e.g., Sick, Vacation): ").strip()
    if not leave_type:
        print("\u26a0️ Leave Type cannot be empty.")
        return

    start_date_input = input("Enter Start Date (YYYY-MM-DD): ").strip()
    try:
        start_date = datetime.strptime(start_date_input, "%Y-%m-%d").date()
    except ValueError:
        print("\u26a0️ Invalid date format. Please use YYYY-MM-DD.")
        return

    end_date_input = input("Enter End Date (YYYY-MM-DD): ").strip()
    try:
        end_date = datetime.strptime(end_date_input, "%Y-%m-%d").date()
    except ValueError:
        print("\u26a0️ Invalid date format. Please use YYYY-MM-DD.")
        return

    if end_date < start_date:
        print("\u26a0️ End Date cannot be earlier than Start Date.")
        return

    reason = input("Enter Leave Reason: ").strip()
    if not reason:
        print("\u26a0️ Leave Reason cannot be empty.")
        return

    try:
        connection = create_connection()
        cursor = connection.cursor()

        # Insert leave request into database
        query = """
        INSERT INTO leave_request (employee_id, leave_type, start_date, end_date, reason)
        VALUES (%s, %s, %s, %s, %s);
        """
        cursor.execute(query, (employee_id, leave_type, start_date, end_date, reason))
        connection.commit()

        print(f"\n✅ Leave request submitted successfully for {user['name']} from {start_date} to {end_date}!")
        logging.info(f"Leave request submitted for Employee ID {employee_id}: {leave_type} from {start_date} to {end_date}.")

    except Exception as e:
        logging.error(f"Error submitting leave request: {e}")
        print(f"\n\u26a0️ Error submitting leave request: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            

def view_leave_status(user):
    print("\n--- 📋 View Leave Status ---")

    employee_id = user['id']
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
        SELECT leave_type, start_date, end_date, reason, status
        FROM leave_requests
        WHERE employee_id = %s
        ORDER BY start_date DESC;
        """
        cursor.execute(query, (employee_id,))
        leave_requests = cursor.fetchall()

        if leave_requests:
            print(f"\nLeave Requests for {user['name']}:\n")
            for leave in leave_requests:
                leave_type, start_date, end_date, reason, status = leave
                print(f"Type: {leave_type}, Start: {start_date}, End: {end_date}, Reason: {reason}, Status: {status}")
        else:
            print("\u26a0️ No leave requests found.")

    except Exception as e:
        logging.error(f"Error retrieving leave requests: {e}")
        print(f"\n\u26a0️ Error retrieving leave requests: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

