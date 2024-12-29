import json
from utils.utils import read_json_db

# function to get notifications
def get_manager_notifications(manager_id):
    data = read_json_db()  
    leave_requests = data.get("leave_requests", [])
    notifications = []

    for leave in leave_requests:
        if leave.get("status") == "Pending":  # Filter berdasarkan status saja
            notifications.append({
                "id": leave.get("leave_request_id"),
                "type": leave.get("leave_type", "Unknown Type"),
                "start": leave.get("start_date", "Unknown Start Date"),
                "end": leave.get("end_date", "Unknown End Date"),
                "reason": leave.get("reason", "No reason provided"),
                "status": leave.get("status", "Unknown Status"),
                "employee_name": leave.get("employee_name", "Unknown Employee")  # Tambahkan jika tersedia
            })
    
    return notifications

# fucntion show manager notifications
def show_manager_notifications(manager_id):
    notifications = get_manager_notifications(manager_id)

    if notifications:
        print("\n--- 🔔 Notifications ---")
        for i, notif in enumerate(notifications, 1):
            message = (
                f"Leave request from {notif['employee_name']} ({notif['type']}) "
                f"from {notif['start']} to {notif['end']} is currently {notif['status']}."
            )
            print(f"{i}. {message}")
            print(f"   Reason: {notif['reason']}\n")
    else:
        print("\n--- 🔔 Notifications ---")
        print("No new notifications at the moment.\n")

