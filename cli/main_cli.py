from auth.auth import login
from pages.admin_dashboard import admin_dashboard
from pages.employee_dashboard import employee_dashboard

def main():
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
            print("\n❌ Role tidak dikenali. Mohon cek kembali data pengguna.")
    
    # if login failed
    else:
        print("\n" + "┌" + "─" * 63 + "┐")
        print("│ ❌  Login Failed. Exiting Program.                             │")
        print("├" + "─" * 63 + "┤")
        print("│ 💡  Tip: Ensure your email and password are correct.           │")
        print("│ 🔁  If you forgot your password, contact your admin.           │")
        print("└" + "─" * 63 + "┘")

if __name__ == "__main__":
    main()
