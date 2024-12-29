from utils.utils import read_json_db
from time import sleep
import pandas as pd
import json

wait = sleep 

# Read the JSON database
with open('configs/worknest.json') as f:
    data = json.load(f)

# Convert data to DataFrames
employees_df = pd.DataFrame(data['employees'])
attendance_df = pd.DataFrame(data['attendances'])
leave_requests_df = pd.DataFrame(data['leave_requests'])

# Calculate total leaves for each employee
leave_totals = leave_requests_df.groupby('employee_id').size().reset_index(name='leave_total')

# Calculate attendace status
attendance_totals = attendance_df.groupby('employee_id').agg(
    total_attendance = ('status', 'count'),
    attended = ('status', lambda x: (x == 'Attend').sum())
).reset_index()

# Merge leave totals and attendance totals
performance_df = pd.merge(leave_totals, attendance_totals, left_on='employee_id', right_on='employee_id', how='left')
performance_df.fillna(0, inplace=True)  # Fill NaN values with 0

def calculate_performance(row):
    leave_count = row['leave_total']
    attendance_percentage = (row['attended'] / row['total_attendance']) * 100 if row['total_attendance'] > 0 else 0

    if leave_count == 0:
        if attendance_percentage > 80:
            return 'Very Good'
        elif 70 <= attendance_percentage <= 80:
            return 'Good'
        elif 50 <= attendance_percentage < 70:
            return 'Average'
        else:
            return 'Bad'
    elif 1 <= leave_count <= 3:
        if attendance_percentage > 85:
            return 'Very Good'
        elif 75 <= attendance_percentage <= 85:
            return 'Good'
        elif 60 <= attendance_percentage < 75:
            return 'Average'
        else:
            return 'Bad'
    elif 3 < leave_count <= 5:
        if attendance_percentage > 90:
            return 'Very Good'
        elif 80 <= attendance_percentage <= 90:
            return 'Good'
        elif 65 <= attendance_percentage < 80:
            return 'Average'
        else:
            return 'Bad'
    else:  # More than 5 leaves
        if attendance_percentage > 95:
            return 'Very Good'
        elif 85 <= attendance_percentage <= 95:
            return 'Good'
        elif 70 <= attendance_percentage < 85:
            return 'Average'
        else:
            return 'Bad'

# Apply performance calculation
performance_df['overall_performance'] = performance_df.apply(calculate_performance, axis=1)

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
    print(f"Comment for Employee ID {employee_id}: {comment}")
    
def reporting_and_analytics():
    wait(3)
    print("\n" + "=" * 60)
    print("                📊 Reporting and Analytics                    ")
    print("=" * 60)
    reporting_table = performance_df[['employee_id', 'leave_total', 'attended', 'total_attendance', 'overall_performance']]
    print(reporting_table.to_string(index=False))
    
    while True:
        print("\n1. Filter Reports (by ID)\n2. Filter Reports (by Performance)\n3. Comment")
        choice = int(input("\n Please select a menu to use (1-3): "))
        if choice == 1:
            employee_id = int(input("\n Enter Employee ID: "))
            filtered_df = filter_performance(performance_df, employee_id=employee_id)
            if filtered_df.empty:
                print('\n No data to be filtered.')
            else:
                print(filtered_df.to_string(index=False))
        elif choice == 2:
            performance = input("\n Enter Performance (e.g. 'Very Good', 'Good', 'Average', and 'Bad': ").capitalize()
            filtered_df = filter_performance(performance_df, performance=performance)
            if filtered_df.empty:
                print('\n No data to be filtered.')
            else:
                print(filtered_df.to_string(index=False))
        elif choice == 3:
            employee_id = input("\n Enter Employee ID: ")
            comment = input("\n Enter Comment: ")
            add_comment(employee_id, comment)
        else:
            print("\n Invalid choice. Please select a valid option!")
            
        input("\nPress Enter to return to Reporting and Analytics menu...")
   