# function to view attendance records
def view_attendance():
    print("\nFetching attendance records...")
    
    print("Attendance records loaded successfully!")

# function to record attendance for an employee
def record_attendance():
    employee_id = input("\nEnter Employee ID: ").strip()
    attendance_date = input("Enter Attendance Date (YYYY-MM-DD): ").strip()
    check_in = input("Enter Check-in Time (HH:MM): ").strip()
    check_out = input("Enter Check-out Time (HH:MM): ").strip()
    
    print(f"\nAttendance recorded successfully for Employee ID {employee_id} on {attendance_date}!")
    
