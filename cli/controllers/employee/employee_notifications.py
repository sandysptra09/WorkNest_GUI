import json
from utils.utils import read_json_db

# function to get notifications
def get_notifications(employee_id):
    data = read_json_db()
    leave_requests = data.get("leave_requests", [])
    notifications = []

    for leave in leave_requests:
        if leave["employee_id"] == employee_id:
            notifications.append({
                "id": leave["leave_request_id"],
                "type": leave["leave_type"],
                "start": leave["start_date"],
                "end": leave["end_date"],
                "reason": leave["reason"],
                "status": leave["status"]
            })

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
