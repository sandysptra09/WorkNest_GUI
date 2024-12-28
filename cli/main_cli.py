from auth.auth import login
from pages.admin_dashboard import admin_dashboard
from pages.employee_dashboard import employee_dashboard
from time import sleep

wait = sleep

def main():
    wait(2)
    print("\n" + "┌" + "─" * 63 + "┐")
    print("│ 🌟  Welcome to WorkNest! 🌟                                   │")
    print("├" + "─" * 63 + "┤")
    print("│ Your trusted platform for employee and admin management.      │")
    print("│ ✨ Empowering productivity and collaboration. ✨              │")
    print("└" + "─" * 63 + "┘")
    
    user = login()

    # if login successful
    if user:  
        print("\n" + "┌" + "─" * 63 + "┐")
        print("│ 🎉  Welcome, {:<49}│".format(user['name'].title()))
        print("│ ✨  Role: {:<52}│".format(user['role'].capitalize()))
        print("└" + "─" * 63 + "┘")
        
        # Pastikan role diperbandingkan dalam format yang sama
        role = user['role'].lower()  
        
        if role == 'admin':  
            admin_dashboard(user)  
        elif role == 'employee':
            employee_dashboard(user)  
        else:
            print("\n❌ Role not found. Please check the user data again.")
    
    # if login failed
    else:
        wait(0.5)
        print("\n" + "┌" + "─" * 63 + "┐")
        wait(0.5)
        print("│ ❌  Login Failed. Exiting Program.                            │")
        wait(1.5)
        print("├" + "─" * 63 + "┤")
        wait(0.5)
        print("│ 💡  Tip: Ensure your email and password are correct.          │")
        wait(0.5)
        print("│ 🔁  If you forgot your password, contact our admin.           │")
        wait(0.5)
        print("└" + "─" * 63 + "┘")

if __name__ == "__main__":
    main()
