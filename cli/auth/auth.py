import json
from getpass import getpass
from utils.utils import read_json_db
from time import sleep

wait = sleep

def login():
    data = read_json_db()  
    # print("Data yang dimuat:", data)
    chance = 3 
    while True:
        sleep(2) 
        try:
            print("\n" + "=" * 60)
            print("🔐 Login to WorkNest")
            print("=" * 60)
            
            email = input("📧  Email: ").strip()
            password = getpass(" Password: ").strip()
            
            if "@" not in email:
                print("\n❌ Invalid!. Email must contain '@'.")
                continue
            
            # find users by email
            user = None
            # check in employees
            for emp in data['employees']:
                if emp['email'] == email:
                    user = emp
                    break
                
            # check in admins if not found in employees
            if not user:
                for admin in data['admins']:
                    if admin['email'] == email:
                        user = admin
                        break
            
            if user:
                if password == user['password']:
                    return user
                if chance == 1:
                    print("\n❌ You have reached out the maximum attempt. Please try again later.")
                    break  
                else:
                    print(f"\n❌ Incorrect password. Try again (You have {chance-1} attempts left).")
                    chance -= 1
                    continue
            else:
                print("\n❌ User not found. Make sure the email you entered is correct. .")
                continue
        
        except Exception as e:
            print(f'\n⚠️ Error on login: {e}')
            
        return None

