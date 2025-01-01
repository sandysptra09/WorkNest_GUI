from controllers.manager.employee_data_management import (
    add_employee,
    view_employee,
    view_all_employees,
    update_employee,
    delete_employee
)
from utils.utils import read_json_db
from time import sleep

wait = sleep

# load existing data from JSON
data = read_json_db()
employees = data.get("employees", [])

# function to manage employee data
def manage_employee_data():
    while True:
        wait(3)
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
        if not choice:
            print("\n⚠️  Fields must not be empty!. Please select a valid feature!.")
            wait(2)            
        elif choice.isdigit():
            choice = int(choice) # Convert choice to integer
            if choice == 1:
                while True:
                    # input for add employee
                    nip = input("Enter employee NIP (must be 8 characters long): ").strip() 
                    if not nip:
                        print("❌ NIP cannot be empty.") # Check if NIP is empty
                        continue
                    try:
                        int(nip) # Conver NIP to an integer
                    except ValueError:
                        print("❌ NIP must be an integer.")
                        continue
                    if len(nip) != 8:  # Check the length of NIP
                        print("❌ NIP must be 8 characters long.")
                        continue
                    if any(emp['nip'] == nip for emp in employees): # Check if NIP already exists
                        print(f"❌ NIP '{nip}' already exists. Please use a unique NIP.")
                    else:
                        break  # Valid NIP
                
                while True:
                    # input for add employee
                    nik = input("Enter employee NIK: ").strip()
                    if not nik:
                        print("❌ NIK cannot be empty.") # Check if NIK is empty
                        continue
                    try:
                        int(nik) # Conver NIK to an integer
                    except ValueError:
                        print("❌ NIK must be an integer.")
                        continue
                    if not (13 <= len(nik) <= 16):  # Check the length of NIK
                        print("❌ NIK must be between 13 and 16 characters long.")
                        continue
                    if any(emp['nik'] == nik for emp in employees): # Check if NIK already exists
                        print(f"❌ NIK '{nik}' already exists. Please use a unique NIK.")
                        continue
                    else:
                        break  # Valid NIK
                
                while True:    
                    name = input("Enter employee's name: ").strip()
                    if not name:
                        print("❌ Name cannot be empty.") # Check if name is empty
                        continue
                    if any(emp['name'] == name for emp in employees): # Check if name already exists
                        print(f"❌ Name '{name}' already exists. Please use another name.")
                        continue
                    if not all(part.isalpha() for part in name.split()): # Check if name contains only alphabets and allows space
                        print("❌ Name must contain only alphabets.")
                        continue
                    else:
                        break  # Valid name
                
                while True:    
                    gender = input("Enter employee's gender (Male/Female): ").strip().lower()
                    if gender not in ['male', 'female']: # Check if gender is valid
                        print("❌ Gender must be either 'Male' or 'Female'.")
                        continue
                    elif not gender:
                        print("❌ Gender cannot be empty.") # Check if gender is empty
                        continue
                    else:
                        break  # Valid gender
                
                while True:    
                    birth_place = input("Enter employee's birth place: ").strip()
                    if not birth_place:
                        print("❌ Birth place cannot be empty.") # Check if birth place is empty
                        continue
                    elif not birth_place.isalpha(): # Check if birth place contains only alphabets
                        print("❌ Birth place must contain only alphabets.")
                        continue
                    else:
                        break  # Valid birth place
            
                while True:    
                    birth_date = input("Enter employee's birth date (YYYY-MM-DD): ").strip()
                    if not birth_date:
                        print("❌ Birth date cannot be empty.") # Check if birth date is empty
                        continue
                    try:
                        from datetime import datetime
                        datetime.strptime(birth_date, "%Y-%m-%d")
                        break  # Valid Date
                    except ValueError:
                        print("❌ Invalid date format. Please use 'YYYY-MM-DD'.")
                        continue
                
                while True:    
                    phone = input("Enter employee's phone (leave blank if not available): ").strip()
                    if phone:
                        if not phone.isdigit(): # Check if phone contains only digits
                            print("❌ Phone must contain only digits.")
                            continue
                        elif len(phone) <= 10: # Check if phone number is 10 digits long
                            print("❌ Phone number must be at least 10 digits long.")
                            continue
                        else:
                            break  # Valid phone number
                    if not phone:
                        phone = None
                        break  # Valid phone number or empty string
                
                while True:  
                    religion = input("Enter employee's religion (leave blank if not available): ").strip()
                    if religion:
                        if not religion.isalpha(): # Check if religion contains only alphabets
                            print("❌ Religion must contain only alphabets.")
                            continue
                        else:
                            break  # Valid religion
                    if not religion:
                        religion = None
                        break  # Valid religion or empty string
                    
                while True:
                    marital_status = input("Enter marital status (Single/Married/Divorced): ").strip().lower()
                    if not marital_status:
                        print("❌ Marital status cannot be empty.")
                        continue
                    if marital_status not in ["single", "married", "divorced"]: # Check
                        print("❌ Invalid marital status. Please choose from 'Single', 'Married', or Divorced")
                        continue
                    else:
                        break  # Valid marital status
                    
                while True:    
                    address = input("Enter employee's address: ").strip()
                    if not address:
                        print("❌ Address cannot be empty.")
                        continue
                    elif len(address) <= 11:
                        print("❌ Address must be at least 11 characters long.")
                        continue
                    else:
                        break  # Valid address
                    
                while True:
                    email = input("Enter employee's email: ").strip()
                    if not email:
                        print("❌ Email cannot be empty.")
                        continue
                    if "@employee.nest" not in email: # Check if email contains "@employee.nest" 
                        print("❌ Email must contain '@employee.nest'.")
                        continue
                    else:
                        break  # Valid email
                
                while True:
                    password = input("Enter employee's password: ").strip()
                    if not password:
                        print("❌ Password cannot be empty.")
                        continue
                    if len(password) < 8: # Check if password is at least 8 characters long
                        print("❌ Password must be at least 8 characters long.")
                        continue
                    else:
                        break  # Valid password
                
                # pass email and password to add_employee
                add_employee(nip, nik, name, gender, birth_place, birth_date, phone, religion, 
                            marital_status, address, email, password)

            elif choice == 2:
                # view employee by ID
                employee_id = input("Enter employee ID: ")
                view_employee(employee_id)

            elif choice == 3:
                # view all employees
                view_all_employees()

            elif choice == 4:
                # update employee
                try:
                    employee_id = int(input("Enter employee ID: "))
                except ValueError:
                    print("Invalid ID. Please enter a numeric value.")
                    continue
                
                while True:
                    name = input("Enter new name (leave blank to keep current): ").strip()
                    if not name:
                        name = None
                        break # No change in name
                    if name:
                        if any(emp['name'] == name for emp in employees):
                            print("❌ Employee with this name already exists.")
                            continue
                        if not all(part.isalpha() for part in name.split()): # Check if name contains only alphabets
                            print("❌ Name must contain only alphabets.")
                            continue
                        else:
                            break  # Valid name
                
                while True:        
                    gender = input("Enter new gender (leave blank to keep current): ").strip().lower()
                    if not gender:
                        gender = None
                        break # No change in gender
                    if gender:
                        if gender not in ['male', 'female']: # Check if gender is valid
                            print("❌ Invalid gender. Please enter 'male' or 'female'.")
                            continue
                        else:
                            break  # Valid gender
                
                while True:        
                    birth_place = input("Enter new birth place (leave blank to keep current): ").strip()
                    if not birth_place:
                        birth_place = None
                        break # No change in birth place
                    if birth_place:
                        if not birth_place.isalpha():
                            print("❌ Birth place must contain only alphabets.")
                            continue
                        else:
                            break  # Valid birth place
                        
                while True:        
                    birth_date = input("Enter new birth date (leave blank to keep current): ").strip()
                    if not birth_date:
                        birth_date = None
                        break # No change in birth date
                    if birth_date:
                        try:
                            from datetime import datetime
                            datetime.strptime(birth_date, '%Y-%m-%d')
                            break  # Valid birth date
                        except ValueError:
                            print("❌ Invalid date format. Please use YYYY-MM-DD.")
                            continue
                    
                while True:
                    phone = input("Enter new phone (leave blank to keep current): ").strip()
                    if not phone:
                        phone = None
                        break # No change in phone
                    if phone:
                        if not phone.isdigit(): # Check if phone contains only digits
                            print("❌ Phone must contain only digits.")
                            continue
                        elif len(phone) <= 10: # Check if phone has 10 digits or less
                            print("❌ Phone number must be at least 10 digits long.")
                            continue
                        else:
                            break  # Valid phone number
                
                while True:
                    religion = input("Enter new religion (leave blank to keep current): ").strip()
                    if not religion:
                        religion = None
                        break # No change in religion
                    if religion:
                        if not religion.isalpha(): # Check if religion contains only alphabets
                            print("❌ Religion must contain only alphabets.")
                            continue
                        else:
                            break  # Valid religion
                        
                while True:
                    marital_status = input("Enter new marital status (leave blank to keep current): ").strip().lower()
                    if not marital_status:
                        marital_status = None
                        break # No change in marital status
                    if marital_status:
                        if marital_status not in ["single", "married", "divorced"]: # Check if marital status is valid
                            print("❌ Invalid marital status. Please choose from 'Single', 'Married', or 'Divorced'")
                            continue
                        else:
                            break  # Valid marital status
                
                while True:      
                    address = input("Enter new address (leave blank to keep current): ").strip()
                    if not address:
                        address = None
                        break # No change in address
                    if address:
                        if len(address) <= 11:  
                            print("❌ Address must be at least 11 characters long.")
                            continue
                        else:
                            break  # Valid address
                        
                save = input("\nSave the changes? (y/n): ").lower()
                if not save:
                    print("\n⚠️  Fields must not be empty!.")
                    wait(1)
                elif save.isalpha():
                    if save == 'y':
                        # Pass the updates as keyword arguments
                        update_employee(
                            employee_id=employee_id,
                            name=name,
                            gender=gender,
                            birth_place=birth_place,
                            birth_date=birth_date,
                            phone=phone,
                            religion=religion,
                            marital_status=marital_status,
                            address=address
                        )
                        print(f"✔️  Employee ID {employee_id} has been successfully updated.")
                    
                    elif save == 'n':
                        print("❌ Update cancelled.")
                        wait(2)
                        continue
                    else:
                        print("❌ Invalid input. Please enter either 'y' or 'n' to save or cancel the changes.")
                else:
                    print("❌ Please only input letters (y/n).")


            elif choice == 5:
                # delete Employee
                employee_id = input("Enter employee ID: ")
                delete_employee(employee_id)

            elif choice == 6:
                wait(2)
                break  
        else:
            print("\n⚠️  Invalid choice. Please try again.")
            wait(2)
        
        input("\nPress Enter to return to Employee Data Management menu...")

