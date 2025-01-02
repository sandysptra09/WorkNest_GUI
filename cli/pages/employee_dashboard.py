from employee_self_service_menu import manage_employee_self_service
from controllers.employee.employee_notifications import get_notifications, get_comments, show_employee_notifications
from time import sleep

wait = sleep

def employee_dashboard(user):
    while True:
        # Mengambil jumlah notifikasi dan komentar untuk karyawan
        notifications = get_notifications(user["id"])
        comments = get_comments(user["id"])

        notifications_count = len(notifications)
        comments_count = len(comments)

        # Total notifikasi adalah jumlah dari notifications dan comments
        total_notifications_count = notifications_count + comments_count

        wait(3)
        print("\n" + "=" * 60)
        print("                🛠️  Employee Self-Service Dashboard                ")
        print("=" * 60)
        
        print("\n")
        print("┌───────────────────────────────────────────────────────────────┐")
        print(f"│  Hello, {user['name']}!                                         │")
        print(f"│  You have {total_notifications_count} new notification(s)!!                             │")
        print("│                                                               │")
        print("│  1. 🛠️  - Employee Self-Service                                │")
        print("│  2. 🔔 - View Notifications                                   │")
        print("│  3. ❌ - Logout                                               │")
        print("└───────────────────────────────────────────────────────────────┘")
        
        choice = input("\nPlease select a feature (1-3): ").strip()
        if choice == '1':
            print("\n--- 🛠️ Employee Self-Service ---")
            manage_employee_self_service(user)
        elif choice == '2':
            show_employee_notifications(user["id"])
        elif choice == '3':
            print("\nLogging out...")
            wait(3)
            break
        else:
            print("\n⚠️ Invalid choice. Please select a valid option (1-3).")
            wait(2)
        
        input("\nPress Enter to return to the employee dashboard...")
