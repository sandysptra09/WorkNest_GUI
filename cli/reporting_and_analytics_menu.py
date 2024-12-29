from utils.utils import read_json_db
from time import sleep
import pandas as pd

wait = sleep 

# load existing data from JSON
data = read_json_db()
employees = data.get("employees", [])

def reporting_and_analytics():
    while True:
        wait(3)
        print("\n" + "=" * 60)
        print("                📊 Reporting and Analytics                    ")
        print("=" * 60)
        
        print("\n") 
        
        
        # 
        choice = input("\nPlease select an option (1-6): ").strip()
        
        # if choice == '1':
        #     view_profile(user)
        # elif choice == '2':
        #     edit_profile(user)
        # elif choice == '3':
        #     view_attendance(user)
        # elif choice == '4':
        #     record_attendance(user)
        # elif choice == '5':
        #     request_leave(user)
        # elif choice == '6':
        #     view_leave_status(user)
        if choice == '7':
            break  
        else:
            
            print("\n⚠️ Invalid choice. Please select a valid option (1-6).")

        input("\nPress Enter to return to Reporting and Analytics menu...")
   