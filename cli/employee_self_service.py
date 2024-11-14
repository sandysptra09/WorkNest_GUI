from controllers.employee.employee_data_management import (
    add_employee,
    view_employee,
    update_employee,
    delete_employee
)

def manage_employee_data_self_service():
    while True:
        # Display the Employee Data Management menu
        print("\n" + "=" * 60)
        print("                📋 Employee Self Service                ")
        print("=" * 60)
        print("\n")
        print("┌───────────────────────────────────────────────────────────────┐")
        print("│  1. ➕  - Add Information                                     |")
        print("│  2. 👁️   - View Profile                                       │")
        print("│  3. ✏️   - Edit Profile                                       │")
        print("│  4. 🗑️   - Delete Profile                                     │")
        print("│  5. 🔙  - Return to Main Menu                                 │")
        print("└───────────────────────────────────────────────────────────────┘")
        
        choice = input("Select an option [1-5]: ")

        if choice == '1':
            name = input("Enter employee's name: ")
            position = input("Enter employee's position: ")
            add_employee(name, position)
        elif choice == '2':
            employee_id = input("Enter employee ID: ")
            view_employee(employee_id)
        elif choice == '3':
            employee_id = input("Enter employee ID: ")
            name = input("Enter new name (leave blank to keep current): ")
            position = input("Enter new position (leave blank to keep current): ")
            update_employee(employee_id, name if name else None, position if position else None)
        elif choice == '4':
            employee_id = input("Enter employee ID: ")
            delete_employee(employee_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
