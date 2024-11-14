# 
from configs.db_connection import create_connection

# function add employee
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
            print(f"Added employee: {name} with position: {marital_status}")
    except Exception as e:
        print(f"Error: {e}")
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
                print(f"ID: {employee[0]}, NIP: {employee[1]}, NIK: {employee[2]}, Name: {employee[3]}, Gender: {employee[4]}, Birth Place: {employee[5]}, Birth Date: {employee[6]}, Phone: {employee[7]}, Religion: {employee[8]}, Marital Status: {employee[9]}, Address: {employee[10]}")
            else:
                print("Employee not found.")
    except Exception as e:
        print(f"Error: {e}")
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
            print(f"Updated employee data for ID: {employee_id}")
    except Exception as e:
        print(f"Error: {e}")
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
            print(f"Deleted employee with ID: {employee_id}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()
