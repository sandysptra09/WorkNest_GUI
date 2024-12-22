import json
from getpass import getpass
from utils.utils import read_json_db

def login():
    data = read_json_db()  
    # print("Data yang dimuat:", data)  
    try:
        print("\n" + "=" * 60)
        print("🔐 Login to WorkNest")
        print("=" * 60)
        
        email = input("📧  Email: ").strip()
        password = getpass(" Password: ").strip()
        
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
            else:
                print("\n❌ Incorrect password. Try again.")
        else:
            print("\n❌ User not found. Make sure the email you entered is correct. .")
    
    except Exception as e:
        print(f'\n⚠️ Error on login: {e}')
        
    return None

