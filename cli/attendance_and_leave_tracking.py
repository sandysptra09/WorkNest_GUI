# attendance_and_leave_tracking.py

from controllers.manager.track_attendance_and_leave import (
    view_attendance,
    record_attendance,
    request_leave,
    view_leave_requests
)

def attendance_and_leave_menu():
    while True:
        print("\n" + "=" * 60)
        print("              🕒 Attendance and Leave Tracking              ")
        print("=" * 60)
        
        print("\n")
        print("┌───────────────────────────────────────────────────────────────┐")
        print("│  1. 👀 - View Attendance Records                              │")
        print("│  2. 📝 - Record Attendance                                    │")
        print("│  3. 🗒️  - Request Leave                                       │")
        print("│  4. 📂 - View Leave Requests                                  │")
        print("│  5. 🔙 - Back to Dashboard                                    │")
        print("└───────────────────────────────────────────────────────────────┘")
        
        choice = input("\nPlease select a feature (1-5): ").strip()
        
        if choice == '1':
            print("\n--- 👀 View Attendance Records ---")
            view_attendance()
        elif choice == '2':
            print("\n--- 📝 Record Attendance ---")
            record_attendance()
        elif choice == '3':
            print("\n--- 🗒️ Request Leave ---")
            request_leave()
        elif choice == '4':
            print("\n--- 📂 View Leave Requests ---")
            view_leave_requests()
        elif choice == '5':
            print("\nReturning to Admin Dashboard...")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a valid option (1-5).")
        
        input("\nPress Enter to return to the menu...")
