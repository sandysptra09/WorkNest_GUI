from utils.utils import read_json_db
from time import sleep
from controllers.manager.reporting_and_analytics import filter_performance, add_reports, calculate_performance
import pandas as pd
import json

wait = sleep 

# Read the JSON database
data = read_json_db()

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

# Apply performance calculation
performance_df['overall_performance'] = performance_df.apply(calculate_performance, axis=1)
    
def reporting_and_analytics():
    while True:
        wait(2)
        print("\n" + "=" * 60)
        print("                📊 Reporting and Analytics                    ")
        print("=" * 60)
        
        # Display the reporting table
        reporting_table = performance_df[['employee_id', 'leave_total', 'attended', 'total_attendance', 'overall_performance']]
        print(reporting_table.to_string(index=False))
        print("\n1. Filter Reports (by ID)\n2. Filter Reports (by Performance)\n3. Reports\n4. 🔙 Return to Main Menu    ")
        choice = input("\n Please select a menu to use (1-4): ")
        if not choice:
            print("\n⚠️  Fields must not be empty!. Please select a valid feature!.")
            wait(2)
            continue
        elif choice.isdigit():
            choice = int(choice)
            if choice == 1:
                while True:
                    employee_id = input("\n Enter Employee ID: ")
                    if not employee_id:
                        print("\n ❌ Employee ID must not be empty!.")
                        continue
                    elif employee_id.isdigit():
                        filtered_df = filter_performance(performance_df, employee_id=int(employee_id))
                        if filtered_df.empty:
                            print("\n ❌ No data to be filtered.")
                            break
                        else:
                            print(filtered_df.to_string(index=False))
                            break
                    else:
                        print("\n ❌ Employee ID must be a number!. Please enter a valid ID!")
                        continue
            elif choice == 2:
                while True:
                    performance = input("\n Enter Performance (e.g. 'Very Good', 'Good', 'Average', and 'Bad'): ").lower()
                    if not performance:
                        print("\n ❌ Performance must not be empty!")
                        continue
                    elif performance in performance_df['overall_performance'].values:
                        filtered_df = filter_performance(performance_df, performance=performance)
                        if not filtered_df.empty:
                            print(filtered_df.to_string(index=False))
                            break
                    else:
                        print("\n ❌ No data to be filtered.")
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
                print("\n--- 🔙 Returning to Admin Dashboard...")
                wait(1)
                break
            else:
                print("\n⚠️ Invalid choice. Please select a valid option (1-4).")
                wait(1)
                input("\nPress Enter to return to Reporting and Analytics menu...")
                continue
        else:
            print("\n⚠️ Please only input numbers (1-4).")
            wait(2)
            input("\nPress Enter to return to Reporting and Analytics menu...")
            continue
        
        input("\nPress Enter to return to Reporting and Analytics menu...")
        continue


