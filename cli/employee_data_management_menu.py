from controllers.manager.employee_data_management import (
    add_employee,
    view_employee,
    view_all_employees,
    update_employee,
    delete_employee
)
from configs.db_connection import create_connection

# function to manage employee data
def manage_employee_data():
    while True:
        # display the Employee Data Management menu
        print("\n" + "=" * 60)
        print("                📋 Employee Data Management                ")
        print("=" * 60)
        print("\n")
        print("┌───────────────────────────────────────────────────────────────┐")
        print("│  1. ➕  - Add Employee                                        │")
        print("│  2. 👁️   - View Employee (by ID)                               │")
        print("│  3. 👀  - View All Employees                                  │")  
        print("│  4. ✏️   - Update Employee                                     │")
        print("│  5. 🗑️   - Delete Employee                                     │")
        print("│  6. 🔙  - Return to Main Menu                                 │")
        print("└───────────────────────────────────────────────────────────────┘")
        
        choice = input("Select an option [1-6]: ")

        if choice == '1':
            # input for add employee
            nip = input("Enter employee NIP: ")
            nik = input("Enter employee NIK: ")
            name = input("Enter employee's name: ")
            gender = input("Enter employee's gender (Male/Female): ")
            birth_place = input("Enter employee's birth place: ")
            birth_date = input("Enter employee's birth date (YYYY-MM-DD): ")
            phone = input("Enter employee's phone (leave blank if not available): ")
            religion = input("Enter employee's religion (leave blank if not available): ")
            marital_status = input("Enter marital status (Single/Married/Divorced): ")
            address = input("Enter employee's address: ")
            email = input("Enter employee's email: ")  
            password = input("Enter employee's password: ")  
            
            # pass email and password to add_employee
            add_employee(nip, nik, name, gender, birth_place, birth_date, phone, religion, 
                         marital_status, address, email, password)

        elif choice == '2':
            # view employee by ID
            employee_id = input("Enter employee ID: ")
            view_employee(employee_id)

        elif choice == '3':
            # view all employees
            view_all_employees()

        elif choice == '4':
            # update employee
            employee_id = input("Enter employee ID: ")
            name = input("Enter new name (leave blank to keep current): ")
            gender = input("Enter new gender (leave blank to keep current): ")
            birth_place = input("Enter new birth place (leave blank to keep current): ")
            birth_date = input("Enter new birth date (leave blank to keep current): ")
            phone = input("Enter new phone (leave blank to keep current): ")
            religion = input("Enter new religion (leave blank to keep current): ")
            marital_status = input("Enter new marital status (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")

            update_employee(employee_id, name, gender, birth_place, birth_date, phone, religion, marital_status, address)

        elif choice == '5':
            # delete Employee
            employee_id = input("Enter employee ID: ")
            delete_employee(employee_id)

        elif choice == '6':
            break  
        else:
            print("Invalid choice. Please try again.")