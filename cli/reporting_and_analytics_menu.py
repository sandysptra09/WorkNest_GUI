from utils.utils import read_json_db
from time import sleep
from controllers.manager.reporting_and_analytics import filter_performance, add_reports, calculate_performance
import pandas as pd
import json

wait = sleep 

data = read_json_db()

# convert data to DataFrames
employees_df = pd.DataFrame(data['employees'])
attendance_df = pd.DataFrame(data['attendances'])
leave_requests_df = pd.DataFrame(data['leave_requests'])

# calculate total leaves for each employee
leave_totals = leave_requests_df.groupby('employee_id').size().reset_index(name='leave_total')

# calculate attendace status
attendance_totals = attendance_df.groupby('employee_id').agg(
    total_attendance = ('status', 'count'),
    attended = ('status', lambda x: (x == 'Attend').sum())
).reset_index()

# merge leave totals and attendance totals
performance_df = pd.merge(leave_totals, attendance_totals, left_on='employee_id', right_on='employee_id', how='left')
performance_df.fillna(0, inplace=True)  # Fill NaN values with 0

# apply performance calculation
performance_df['overall_performance'] = performance_df.apply(calculate_performance, axis=1)
    
def reporting_and_analytics():
    wait(3)
    print("\n" + "=" * 60)
    print("                📊 Reporting and Analytics                    ")
    print("=" * 60)
    reporting_table = performance_df[['employee_id', 'leave_total', 'attended', 'total_attendance', 'overall_performance']]
    print(reporting_table.to_string(index=False))
    
    while True:
        print("\n1. Filter Reports (by ID)\n2. Filter Reports (by Performance)\n3. Reports\n4. 🔙 Return to Main Menu    ")
        choice = int(input("\n Please select a menu to use (1-4): "))
        if choice == 1:
            employee_id = input("\n Enter Employee ID: ")
            if not employee_id:
                print("\n ❌ Employee ID must not be empty!.")
            elif employee_id.isdigit():
                filtered_df = filter_performance(performance_df, employee_id=int(employee_id))
                if filtered_df.empty:
                    print("\n ❌ No data to be filtered.")
                else:
                    print(filtered_df.to_string(index=False))
            else:
                print("\n ❌ Employee ID must be a number!. Please enter a valid ID!")
        elif choice == 2:
            performance = input("\n Enter Performance (e.g. 'Very Good', 'Good', 'Average', and 'Bad'): ").lower()
            if not performance:
                print("\n ❌ Performance must not be empty!")
            elif performance in performance_df['overall_performance'].values:
                filtered_df = filter_performance(performance_df, performance=performance)
                if filtered_df.empty:
                    print('\n ❌ No data to be filtered.')
                else:
                    print(filtered_df.to_string(index=False))
            else:
                print("\n ❌ Performance does not exist!. Please enter a valid performance!")
        elif choice == 3:
            while True:
                employee_id = input("\n Enter Employee ID: ").strip()
                if not employee_id:
                    print('\n ❌ Employee ID must not be empty!')
                elif not employee_id.isdigit():
                    print("\n ❌ Employee ID must be a number! Please enter a valid ID.")
                else:
                    break 

            while True:
                subject = input("\n Enter Subject: ").strip()
                if not subject:
                    print("\n ❌ Subject must not be empty!")
                else:
                    break

            while True:
                description = input("\n Enter Description: ").strip()
                if not description:
                    print("\n ❌ Description must not be empty!")
                elif len(description) < 10:
                    print("\n ❌ Description must be at least 10 characters long!")
                else:
                    break  

            add_reports(employee_id, subject, description)

        elif choice == 4:
            break
        else:
            print("\n ❌ Invalid choice. Please select a valid option!")
        
        input("\nPress Enter to return to Reporting and Analytics menu...")
   