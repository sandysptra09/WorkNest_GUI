from employee_data_management_menu import manage_employee_data
from attendance_and_leave_tracking import attendance_and_leave_menu
from reporting_and_analytics_menu import reporting_and_analytics
from controllers.manager.manager_notifications import get_manager_notifications, show_manager_notifications
from time import sleep

wait = sleep

def admin_dashboard(user):
    while True:
        notifications = get_manager_notifications(user["id"])
        notifications_count = len(notifications)

        wait(3)
        print("\n" + "=" * 60)
        print("                🏢 Admin Management Dashboard                ")
        print("=" * 60)
        
        print("\n")
        print("┌───────────────────────────────────────────────────────────────┐")
        print(f"│  Hello, {user['name']}!                                        │")
        print(f"│  You have {notifications_count} new notification(s)!!                             │")
        print("│                                                               │")
        print("│  1. 📋 - Employee Data Management                             │")
        print("│  2. 🕒 - Attendance and Leave Tracking                        │")
        print("│  3. 📊 - Reporting and Analytics                              │")
        print("│  4. 🔔 - View Notifications                                   │")
        print("│  5. ❌ - Logout                                               │")
        print("└───────────────────────────────────────────────────────────────┘")
        
        choice = input("\nPlease select a feature (1-5): ").strip()
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
            print("\n--- 🔔 Notifications ---")
            show_manager_notifications(user["id"])
        elif choice == '5':
            print("\nLogging out...")
            wait(3)
            break
        else:
            print("\n⚠️ Invalid choice. Please select a valid option (1-5).")
            wait(2)
        
        input("\nPress Enter to return to the admin dashboard...")
