# main.py
from employee_data_management_menu import manage_employee_data
from employee_self_service import manage_employee_data_self_service


def display_dashboard():
    while True:
        # display the dashboard
        print("\n" + "=" * 60)
        print("                🏢 WorkNest Management Dashboard                ")
        print("=" * 60)
        
        print("\n")
        print("┌───────────────────────────────────────────────────────────────┐")
        print("│  1. 📋 - Employee Data Management                             │")
        print("│  2. 🕒 - Attendance and Leave Tracking                        │")
        print("│  3. 🛠️  - Employee Self-Service                                │")
        print("│  4. 📊 - Reporting and Analytics                              │")
        print("│  5. 🔒 - Role-Based Security and Access Control               │")
        print("│  6. ❌ - Exit Dashboard                                       │")
        print("└───────────────────────────────────────────────────────────────┘")
        
        # prompt user for input and handle a choice
        choice = input("\nPlease select a feature (1-6): ").strip()

        # handle user choice and call appropriate functions
        if choice == '1':
            print("\n--- 📋 Employee Data Management ---")
            manage_employee_data()
        elif choice == '2':
            print("\n--- 🕒 Attendance and Leave Tracking ---")
            print("This feature is currently under development. (Placeholder)")
        elif choice == '3':
            print("\n--- 🛠️ Employee Self-Service ---")
            manage_employee_data_self_service()
        elif choice == '4':
            print("\n--- 📊 Reporting and Analytics ---")
            print("This feature is currently under development. (Placeholder)")
        elif choice == '5':
            print("\n--- 🔒 Role-Based Security and Access Control ---")
            print("This feature is currently under development. (Placeholder)")
        elif choice == '6':
            print("\nThank you for using the WorkNest Management Dashboard. Exiting...")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a valid option (1-6).")
        
        # pause for user input before returning to the main menu
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    print("Initializing Main CLI...\n")
    display_dashboard()

