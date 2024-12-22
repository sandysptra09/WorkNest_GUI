from controllers.employee.employee_self_sevice import (
    view_profile,
    view_attendance,
    record_attendance,
    submit_leave_request,
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
        print("│  2. 🗓️    - View Attendance Records                            │")
        print("│  3. ✉️    - Record Attendance                                  │")
        print("│  4. 📊   - Submit Leave Request                               │")
        print("│  5. 📋   - View Leave Requests                                │")
        print("│  6. 🔙   - Back to Dashboard                                  │")
        print("└───────────────────────────────────────────────────────────────┘")
        
        # 
        choice = input("\nPlease select an option (1-6): ").strip()
        
        if choice == '1':
            view_profile(user)
        elif choice == '2':
            view_attendance(user)
        elif choice == '3':
            record_attendance(user)
        elif choice == '4':
            submit_leave_request(user)
        elif choice == '5':
            view_leave_status(user)
        elif choice == '6':
            break  
        else:
            
            print("\n⚠️ Invalid choice. Please select a valid option (1-6).")

        input("\nPress Enter to return to Employee Self-Service menu...")

