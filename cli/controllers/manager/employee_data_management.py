import bcrypt
from configs.db_connection import create_connection

# function to add employee
def add_employee(nip, nik, name, gender, birth_place, birth_date, phone, religion, marital_status, address, email, password):
    try:
        connection = create_connection()
        with connection.cursor() as cursor:
            # hash the password before saving it to the database
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')
            
            query = """
                INSERT INTO employees (nip, nik, name, gender, birth_place, birth_date, phone, religion, marital_status, address, email, password) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (nip, nik, name, gender, birth_place, birth_date, phone, religion, marital_status, address, email, hashed_password))
            connection.commit()
            
            # success message
            print(f"\n{'=' * 60}")
            print(f"🎉 Employee Successfully Added!")
            print(f"{'-' * 60}")
            print(f"📄 Name           : {name}")
            print(f"📌 Position       : {marital_status}")
            print(f"🆔 NIP            : {nip}")
            print(f"🆔 NIK            : {nik}")
            print(f"🌍 Birth Place    : {birth_place}")
            print(f"🎂 Birth Date     : {birth_date}")
            print(f"📱 Phone          : {phone}")
            print(f"🙏 Religion       : {religion}")
            print(f"🏡 Address        : {address}")
            print(f"📧 Email          : {email}")
            print(f"{'=' * 60}\n")
            
    except Exception as e:
        print(f"\n❌ Error occurred while adding employee: {e}")
    finally:
        connection.close()



# function to view employee details by ID
def view_employee(employee_id):
    try:
        connection = create_connection()
        with connection.cursor() as cursor:
            query = "SELECT * FROM employees WHERE id = %s"
            cursor.execute(query, (employee_id,))
            employee = cursor.fetchone()
            if employee:
                print(f"\n{'='*60}")
                print(f"📋  Employee Details (ID: {employee[0]})")
                print(f"  NIP: {employee[1]}")
                print(f"  NIK: {employee[2]}")
                print(f"  Name: {employee[3]}")
                print(f"  Gender: {employee[4]}")
                print(f"  Birth Place: {employee[5]}")
                print(f"  Birth Date: {employee[6]}")
                print(f"  Phone: {employee[7]}")
                print(f"  Religion: {employee[8]}")
                print(f"  Marital Status: {employee[9]}")
                print(f"  Address: {employee[10]}")
                print(f"{'='*60}")
            else:
                print("\nEmployee not found.")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        connection.close()
        
# function to view all employees
def view_all_employees():
    try:
        connection = create_connection()
        with connection.cursor() as cursor:
            query = "SELECT * FROM employees"
            cursor.execute(query)
            employees = cursor.fetchall()

            if employees:
                print("\n" + "=" * 60)
                print("📋  All Employees")
                print("=" * 60)
                for employee in employees:
                    print(f"\n{'=' * 60}")
                    print(f"ID: {employee[0]}")
                    print(f"NIP: {employee[1]}")
                    print(f"NIK: {employee[2]}")
                    print(f"Name: {employee[3]}")
                    print(f"Gender: {employee[4]}")
                    print(f"Birth Place: {employee[5]}")
                    print(f"Birth Date: {employee[6]}")
                    print(f"Phone: {employee[7]}")
                    print(f"Religion: {employee[8]}")
                    print(f"Marital Status: {employee[9]}")
                    print(f"Address: {employee[10]}")
                    print(f"{'=' * 60}")
                print("\n" + "=" * 60)
            else:
                print("\nNo employees found.")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        connection.close()

# function to update employee details with confirmation
def update_employee(employee_id, name=None, gender=None, birth_place=None, birth_date=None, phone=None, religion=None, marital_status=None, address=None):
    confirmation = input("Are you sure you want to update this employee's data? (yes/no): ").strip().lower()
    if confirmation != 'yes':
        print("Update canceled.")
        return

    try:
        connection = create_connection()
        with connection.cursor() as cursor:
            updates = []
            values = []
            
            # Collect fields to update
            if name:
                updates.append("name = %s")
                values.append(name)
            if gender:
                updates.append("gender = %s")
                values.append(gender)
            if birth_place:
                updates.append("birth_place = %s")
                values.append(birth_place)
            if birth_date:
                updates.append("birth_date = %s")
                values.append(birth_date)
            if phone:
                updates.append("phone = %s")
                values.append(phone)
            if religion:
                updates.append("religion = %s")
                values.append(religion)
            if marital_status:
                updates.append("marital_status = %s")
                values.append(marital_status)
            if address:
                updates.append("address = %s")
                values.append(address)

            # handle no updates case
            if not updates:
                print("No updates provided. Nothing to update.")
                return

            values.append(employee_id)
            query = f"UPDATE employees SET {', '.join(updates)} WHERE id = %s"
            cursor.execute(query, values)
            connection.commit()

            # Feedback on result
            if cursor.rowcount > 0:
                print(f"\n{'='*60}")
                print(f"✏️  Updated Employee Data for ID: {employee_id}")
                print(f"{'='*60}")
            else:
                print("No data was updated. Please check the input values.")
    except Exception as e:
        connection.rollback()
        print(f"\nError: {e}")
    finally:
        connection.close()


# function to delete employee with confirmation
def delete_employee(employee_id):
    if not employee_id or not isinstance(employee_id, int):
        print("Invalid employee ID.")
        return

    try:
        connection = create_connection()
        with connection.cursor() as cursor:
            # check if employee exists
            cursor.execute("SELECT name, nip FROM employees WHERE id = %s", (employee_id,))
            employee = cursor.fetchone()
            if not employee:
                print(f"No employee found with ID: {employee_id}")
                return

            # display employee info for confirmation
            print(f"Employee to be deleted:")
            print(f"Name: {employee[0]}, NIP: {employee[1]}")

            # ask for confirmation
            confirmation = input("Are you sure you want to delete this employee? (yes/no): ").strip().lower()
            if confirmation != 'yes':
                print("Deletion canceled.")
                return

            # delete the employee
            query = "DELETE FROM employees WHERE id = %s"
            cursor.execute(query, (employee_id,))
            connection.commit()

            # feedback on deletion
            if cursor.rowcount > 0:
                print(f"\n{'='*60}")
                print(f"🗑️  Deleted Employee: {employee[0]} (ID: {employee_id})")
                print(f"{'='*60}")
            else:
                print(f"No data was deleted. Employee ID {employee_id} may not exist.")
    except Exception as e:
        connection.rollback()
        print(f"\nError: {e}")
    finally:
        connection.close()
