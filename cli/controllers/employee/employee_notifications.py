import json
from utils.utils import read_json_db

# function to get notifications
def get_notifications(employee_id):
    data = read_json_db()
    all_notifications = data.get("notifications", [])
    notifications = [
        notif for notif in all_notifications if notif["employee_id"] == employee_id
    ]
    return notifications


# function to show notifications for a specific employee
def show_employee_notifications(employee_id):

    notifications = get_notifications(employee_id)

    if notifications:
        print("\n--- 🔔 Notifications ---")
        for i, notif in enumerate(notifications, 1):
            message = (
                f"Leave request for {notif['type']} from {notif['start']} "
                f"to {notif['end']} has been {notif['status']}."
            )
            print(f"{i}. {message}")
            print(f"   Reason: {notif['reason']}\n")
    else:
        print("\n--- 🔔 Notifications ---")
        print("No new notifications at the moment.\n")
