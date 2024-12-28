from employee_data_management_menu import manage_employee_data
from attendance_and_leave_tracking import attendance_and_leave_menu
from reporting_and_analytics_menu import reporting_and_analytics
from time import sleep

wait = sleep

# add user as parameter
def admin_dashboard(user):  
    while True:
        wait(3)
        print("\n" + "=" * 60)
        print("                🏢 Admin Management Dashboard                ")
        print("=" * 60)
        
        print("\n")
        print("┌───────────────────────────────────────────────────────────────┐")
        print(f"│  Hello, {user['name']}!                                        │")
        print(f"│  You have 6 new notifications!!                                │")
        print("│  1. 📋 - Employee Data Management                             │")
        print("│  2. 🕒 - Attendance and Leave Tracking                        │")
        print("│  3. 📊 - Reporting and Analytics                              │")
        print("│  4. ❌ - Logout                                               │")
        print("└───────────────────────────────────────────────────────────────┘")
        
        choice = input("\nPlease select a feature (1-4): ").strip()
        if choice == '1':
            print("\n--- 📋 Employee Data Management ---")
            manage_employee_data()
        elif choice == '2':
            print("\n--- 🕒 Attendance and Leave Tracking ---")
            attendance_and_leave_menu()
        elif choice == '3':
            print("\n--- 📊 Reporting and Analytics ---")
            reporting_and_analytics()
        elif choice == '4':
            print("\nLogging out...")
            wait(3)
            break
        else:
            print("\n⚠️ Invalid choice. Please select a valid option (1-4).")
            wait(2)
        
        input("\nPress Enter to return to the admin dashboard...")
