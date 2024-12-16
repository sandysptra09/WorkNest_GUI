from employee_self_service_menu import manage_employee_self_service

# add user as parameter
def employee_dashboard(user):
    while True:
        print("\n" + "=" * 60)
        print("                🛠️ Employee Self-Service Dashboard                ")
        print("=" * 60)
        
        print("\n")
        print("┌───────────────────────────────────────────────────────────────┐")
        print("│  1. 🛠️  - Employee Self-Service                                │")
        print("│  2. ❌ - Logout                                               │")
        print("└───────────────────────────────────────────────────────────────┘")
        
        choice = input("\nPlease select a feature (1-2): ").strip()
        if choice == '1':
            print("\n--- 🛠️ Employee Self-Service ---")
            manage_employee_self_service(user)
        elif choice == '2':
            print("\nLogging out...")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a valid option (1-2).")
        
        input("\nPress Enter to return to the employee dashboard...")
