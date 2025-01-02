import json
from utils.utils import read_json_db

# function to get notifications
def get_manager_notifications(manager_id):
    data = read_json_db()  
    notifications_data = data.get("notifications", [])
    notifications = []

    for notif in notifications_data:
        if notif.get("status") == "Pending":  # Filter berdasarkan status Pending
            notifications.append({
                "id": notif.get("id"),
                "type": notif.get("type", "Unknown Type"),
                "start": notif.get("start", "Unknown Start Date"),
                "end": notif.get("end", "Unknown End Date"),
                "reason": notif.get("reason", "No reason provided"),
                "status": notif.get("status", "Unknown Status"),
                "employee_id": notif.get("employee_id")
            })
    
    return notifications

# function to show manager notifications
def show_manager_notifications(manager_id):
    notifications = get_manager_notifications(manager_id)

    if notifications:
        print("\n--- 🔔 Notifications ---")
        for i, notif in enumerate(notifications, 1):
            message = (
                f"Leave request (Type: {notif['type']}) "
                f"from {notif['start']} to {notif['end']} is currently {notif['status']}."
            )
            print(f"{i}. {message}")
            print(f"   Reason: {notif['reason']}\n")
    else:
        print("\n--- 🔔 Notifications ---")
        print("No new notifications at the moment.\n")

