import json
from utils.utils import read_json_db

# Fungsi untuk mengambil notifikasi
def get_notifications(employee_id):
    data = read_json_db()
    all_notifications = data.get("notifications", [])
    notifications = [
        notif for notif in all_notifications if notif["employee_id"] == employee_id
    ]
    return notifications

# fungsi untuk mengambil komentar berdasarkan employee_id
def get_comments(employee_id):
    data = read_json_db()
    all_comments = data.get("comments", [])
    comments = [
        comment for comment in all_comments if comment["employee_id"] == employee_id
    ]
    return comments

# function to show all notifications
def show_employee_notifications(employee_id):
    notifications = get_notifications(employee_id)
    comments = get_comments(employee_id)

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

    if comments:
        print("\n--- 📩 Comments ---")
        for i, comment in enumerate(comments, 1):
            print(f"{i}. {comment['subject']} - {comment['description']} (From: {comment['from']})")
    else:
        print("\n--- 📩 Comments ---")
        print("No new comments at the moment.\n")

