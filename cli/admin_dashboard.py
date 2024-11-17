from employee_data_management_menu import manage_employee_data

# add user as parameter
def admin_dashboard(user):  
    while True:
        print("\n" + "=" * 60)
        print("                🏢 Admin Management Dashboard                ")
        print("=" * 60)
        
        print("\n")
        print("┌───────────────────────────────────────────────────────────────┐")
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
            print("This feature is under development. (Placeholder)")
        elif choice == '3':
            print("\n--- 📊 Reporting and Analytics ---")
            print("This feature is under development. (Placeholder)")
        elif choice == '4':
            print("\nLogging out...")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a valid option (1-4).")
        
        input("\nPress Enter to return to the admin dashboard...")
