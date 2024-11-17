from auth import login
from admin_dashboard import admin_dashboard
from employee_dashboard import employee_dashboard

def main():
    print("Welcome to WorkNest CLI!")
    user = login()  # Panggil fungsi login

    # if login successful
    if user:  
        if user['role'] == 'admin':  
            admin_dashboard(user)  
        else:
            employee_dashboard(user)  
    
    # if login failed
    else:
        print("\n❌ Login failed. Exiting program.")

if __name__ == "__main__":
    main()
