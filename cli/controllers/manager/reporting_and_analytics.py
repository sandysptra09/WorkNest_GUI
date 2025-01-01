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
    else:  # More than 5 leaves
        if attendance_percentage > 95:
            return 'very good'
        elif 85 <= attendance_percentage <= 95:
            return 'good'
        elif 70 <= attendance_percentage < 85:
            return 'average'
        else:
            return 'bad'
        
# Function to filter by performance and employee ID
def filter_performance(performance_df, performance=None, employee_id=None):
    if performance:
        performance_df = performance_df[performance_df['overall_performance'] == performance]
    if employee_id:
        performance_df = performance_df[performance_df['employee_id'] == employee_id]
    return performance_df

# Function to add comments
def add_comment(employee_id, comment):
    # Here you would typically save the comment to a database or file
    print(f" Comment for Employee ID {employee_id}: {comment}")