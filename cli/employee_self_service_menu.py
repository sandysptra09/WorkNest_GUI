from controllers.employee.employee_self_sevice import (
    view_profile,
    edit_profile,
    view_attendance,
    record_attendance,
    request_leave,
    view_leave_status
    # track_performance
)

def manage_employee_self_service(user):
    while True:
        print("\n" + "=" * 60)
        print("                🛠️ Employee Self-Service                    ")
        print("=" * 60)
        
        print("\n") 
        
        print("┌───────────────────────────────────────────────────────────────┐")
        print("│  1. 📄   - View Profile                                       │")
        print("│  2. ✏️    - Edit Profile                                       │")
        print("│  3. 🗓️    - View Attendance Records                            │")
        print("│  4. ✉️    - Record Attendance                                  │")
        print("│  5. 📊   - Submit Leave Request                               │")
        print("│  6. 📋   - View Leave Requests                                │")
        print("│  7. 🔙   - Back to Dashboard                                  │")
        print("└───────────────────────────────────────────────────────────────┘")
        
        # 
        choice = input("\nPlease select an option (1-6): ").strip()
        
        if choice == '1':
            view_profile(user)
        elif choice == '2':
            edit_profile(user)
        elif choice == '3':
            view_attendance(user)
        elif choice == '4':
            record_attendance(user)
        elif choice == '5':
            request_leave(user)
        elif choice == '6':
            view_leave_status(user)
        elif choice == '7':
            break  
        else:
            
            print("\n⚠️ Invalid choice. Please select a valid option (1-6).")

        input("\nPress Enter to return to Employee Self-Service menu...")

