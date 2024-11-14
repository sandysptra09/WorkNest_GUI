from configs.db_connection import create_connection

# Function to add employee
def add_employee(nip, nik, name, gender, birth_place, birth_date, phone, religion, marital_status, address):
    try:
        connection = create_connection()
        with connection.cursor() as cursor:
            query = """
                INSERT INTO employees (nip, nik, name, gender, birth_place, birth_date, phone, religion, marital_status, address) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (nip, nik, name, gender, birth_place, birth_date, phone, religion, marital_status, address))
            connection.commit()
            print(f"\n{'='*60}")
            print(f"📋  Employee Added: {name}")
            print(f"  - Position: {marital_status}")
            print(f"{'='*60}")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        connection.close()

# Function to view employee details by ID
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

# Function to update employee details
def update_employee(employee_id, name=None, gender=None, birth_place=None, birth_date=None, phone=None, religion=None, marital_status=None, address=None):
    try:
        connection = create_connection()
        with connection.cursor() as cursor:
            updates = []
            values = []
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

            values.append(employee_id)
            query = f"UPDATE employees SET {', '.join(updates)} WHERE id = %s"
            cursor.execute(query, values)
            connection.commit()
            print(f"\n{'='*60}")
            print(f"✏️  Updated Employee Data for ID: {employee_id}")
            print(f"{'='*60}")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        connection.close()

# Function to delete employee
def delete_employee(employee_id):
    try:
        connection = create_connection()
        with connection.cursor() as cursor:
            query = "DELETE FROM employees WHERE id = %s"
            cursor.execute(query, (employee_id,))
            connection.commit()
            print(f"\n{'='*60}")
            print(f"🗑️  Deleted Employee with ID: {employee_id}")
            print(f"{'='*60}")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        connection.close()
