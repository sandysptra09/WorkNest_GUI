import json
from utils.utils import read_json_db, save_data

# function to calculate performance of employees
def calculate_performance(row):
    leave_count = row['leave_total']
    attendance_percentage = (row['attended'] / row['total_attendance']) * 100 if row['total_attendance'] > 0 else 0

    if leave_count == 0:
        if attendance_percentage > 80:
            return 'very good'
        elif 70 <= attendance_percentage <= 80:
            return 'good'
        elif 50 <= attendance_percentage < 70:
            return 'average'
        else:
            return 'bad'
    elif 1 <= leave_count <= 3:
        if attendance_percentage > 85:
            return 'very good'
        elif 75 <= attendance_percentage <= 85:
            return 'good'
        elif 60 <= attendance_percentage < 75:
            return 'average'
        else:
            return 'bad'
    elif 3 < leave_count <= 5:
        if attendance_percentage > 90:
            return 'very good'
        elif 80 <= attendance_percentage <= 90:
            return 'good'
        elif 65 <= attendance_percentage < 80:
            return 'average'
        else:
            return 'bad'
    else:  
        if attendance_percentage > 95:
            return 'very good'
        elif 85 <= attendance_percentage <= 95:
            return 'good'
        elif 70 <= attendance_percentage < 85:
            return 'average'
        else:
            return 'bad'
        
# function to filter by performance and employee ID
def filter_performance(performance_df, performance=None, employee_id=None):
    if performance:
        performance_df = performance_df[performance_df['overall_performance'] == performance]
    if employee_id:
        performance_df = performance_df[performance_df['employee_id'] == employee_id]
    return performance_df

# function to add comments
def add_reports(employee_id, subject, description):
    data = read_json_db()

    employees = data.get("employees", [])

    # validate that 'employees' exists and is not empty
    if not employees:
        print("\n❌ No employees data found in the database.")
        return

    # validate that 'employee_id' is a valid number
    try:
        employee_id = int(employee_id)  # Pastikan employee_id adalah integer
    except ValueError:
        print("\n❌ Employee ID must be a valid integer!")
        return

    # find employee by ID with validation to avoid None in 'employee_id'
    employee = next((emp for emp in employees if emp.get('id') == employee_id), None)
    
    if not employee:
        print(f"\n❌ Employee with ID {employee_id} not found.")
        return

    to_email = employee.get('email', 'N/A')

    # generate comment ID
    comment_id = len(data.get('comments', [])) + 1

    comment = {
        "comments_id": comment_id,
        "employee_id": employee_id,
        "subject": subject,
        "description": description,
        "from": 'Manager',
        "to": to_email
    }

    if 'comments' not in data:
        data['comments'] = []
    data['comments'].append(comment)
    save_data(data)

    print("\n✔️  Report added successfully!")
