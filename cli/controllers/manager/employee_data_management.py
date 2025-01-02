import json
from utils.utils import read_json_db, save_data

# function to add employee
def add_employee(nip, nik, name, gender, birth_place, birth_date, phone, religion, marital_status, address, email, password):
    
    # load existing data from JSON
    data = read_json_db()
    employees = data.get("employees", [])
    
    # calculate new ID (auto-increment)
    new_id = employees[-1]["id"] + 1 if employees else 1

    # create new employee data
    employee = {
        "id": new_id,  
        "nip": nip,
        "nik": nik,
        "name": name,
        "gender": gender,
        "birth_place": birth_place,
        "birth_date": birth_date,
        "phone": phone,
        "religion": religion,
        "marital_status": marital_status,
        "address": address,
        "email": email,
        "password": password,
        'role': 'Employee',
    }

    # append the new employee to the employees list
    employees.append(employee)

    # save the updated data back to the JSON file
    save_data(data)
    
    # success message
    print(f"\n{'=' * 60}")
    print(f"🎉 Employee Successfully Added!")
    print(f"{'-' * 60}")
    print(f"📄 Name           : {name}")
    print(f"🆔 NIP            : {nip}")
    print(f"🆔 NIK            : {nik}")
    print(f"🌍 Birth Place    : {birth_place}")
    print(f"🎂 Birth Date     : {birth_date}")
    print(f"📱 Phone          : {phone}")
    print(f"🙏 Religion       : {religion}")
    print(f"🏡 Address        : {address}")
    print(f"📧 Email          : {email}")
    print(f"{'=' * 60}\n")

# function to view employee details by ID
def view_employee(employee_id):
    try:
        # Convert input ID to integer
        employee_id = int(employee_id)
    except ValueError:
        print("Invalid ID format. Please enter a numeric ID.")
        return

    data = read_json_db()
    
    # Find the employee with matching ID
    employee = next((e for e in data["employees"] if e["id"] == employee_id), None)
    
    if employee:
        print(f"\n{'='*60}")
        print(f"📋  Employee Details (ID: {employee['id']})")
        print(f"  NIP           : {employee['nip']}")
        print(f"  NIK           : {employee['nik']}")
        print(f"  Name          : {employee['name']}")
        print(f"  Gender        : {employee['gender']}")
        print(f"  Birth Place   : {employee['birth_place']}")
        print(f"  Birth Date    : {employee['birth_date']}")
        print(f"  Phone         : {employee['phone']}")
        print(f"  Religion      : {employee['religion']}")
        print(f"  Marital Status: {employee['marital_status']}")
        print(f"  Address       : {employee['address']}")
        print(f"{'='*60}")
    else:
        print("\nEmployee not found.")

# function to view all employees
def view_all_employees():
    data = read_json_db()
    employees = data.get("employees", [])
    
    if employees:
        print("\n" + "=" * 60)
        print("📋  All Employees")
        print("=" * 60)
        for employee in employees:
            print(f"\n{'=' * 60}")
            print(f"ID            : {employee['id']}")
            print(f"NIP           : {employee['nip']}")
            print(f"NIK           : {employee['nik']}")
            print(f"Name          : {employee['name']}")
            print(f"Gender        : {employee['gender']}")
            print(f"Birth Place   : {employee['birth_place']}")
            print(f"Birth Date    : {employee['birth_date']}")
            print(f"Phone         : {employee['phone']}")
            print(f"Religion      : {employee['religion']}")
            print(f"Marital Status: {employee['marital_status']}")
            print(f"Address       : {employee['address']}")
            print(f"{'=' * 60}")
    else:
        print("\nNo employees found.")



# function to update employee details with confirmation
def update_employee(employee_id, **updates):
    data = read_json_db()
    employees = data.get("employees", [])
    employee = next((e for e in employees if e["id"] == employee_id), None)
    
    if not employee:
        print("Employee not found.")
        return

    # Apply updates
    for key, value in updates.items():
        if key in employee and value:
            employee[key] = value

    save_data(data)
    print(f"✏️  Updated Employee Data for ID: {employee_id}")


# function to delete employee with confirmation
def delete_employee(employee_id):
    data = read_json_db()
    employees = data.get("employees", [])

    # validate if there are employees in the database
    if not employees:
        print("No employees found in the database.")
        return

    while True:
        employee_id = input("Enter Employee ID to delete: ")

        # validate 
        if not employee_id.isdigit():
            print("❌ Invalid ID. Please enter a numeric value.")
            continue

        employee_id = int(employee_id)

        # get employee by ID
        employee = next((e for e in employees if e["id"] == employee_id), None)
        if not employee:
            print(f"❌ Employee with ID {employee_id} not found. Try again.")
            continue

        # delete employee
        employees.remove(employee)
        save_data(data)
        print(f"🗑️  Deleted Employee: {employee['name']} (ID: {employee_id})")
        break  # Keluar dari loop setelah berhasil menghapus karyawan


