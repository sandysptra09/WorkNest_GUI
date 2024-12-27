from controllers.manager.track_attendance_and_leave import (
    view_attendance,
    view_leave_requests,
    manage_leave_requests
)
from utils.utils import read_json_db

def attendance_and_leave_menu():
    while True:
        print("\n" + "=" * 60)
        print("              🕒 Attendance and Leave Tracking              ")
        print("=" * 60)
        
        print("\n")
        print("┌───────────────────────────────────────────────────────────────┐")
        print("│  1. 📂 - View Attendance Records                              │")
        print("│  2. 📂 - View Leave Requests                                  │")
        print("│  3. 📝 - Manage Leave Requests                                │")
        print("│  4. 🔙 - Back to Dashboard                                    │")
        print("└───────────────────────────────────────────────────────────────┘")
        
        choice = input("\nPlease select a feature (1-4): ").strip()
        
        data = read_json_db() 
        leave_requests = data.get("leave_requests", [])

        if choice == '1':
            print("\n--- 👀 View Attendance Records ---")
            view_attendance()
        elif choice == '2':
            print("\n--- 📝 View Leave Requests ---")
            view_leave_requests()
        elif choice == '3':
            print("\n--- 🗒️ Manage Leave Requests ---")
            manage_leave_requests(leave_requests)
        elif choice == '4':
            print("\n--- 🔙 Returning to Admin Dashboard...")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a valid option (1-4).")
        
        input("\nPress Enter to return to the menu...")