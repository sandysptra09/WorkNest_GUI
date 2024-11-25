import tkinter as tk
from tkinter import messagebox, ttk

def mark_attendance(self):
    selected_employee_index = self.employee_listbox.curselection()
    if not selected_employee_index:
        messagebox.showerror("Error", "Silakan pilih karyawan untuk menandai kehadiran.")
        return
        
    selected_employee = self.karyawan_data[selected_employee_index[0]]
    username = selected_employee['username']
        
    if username not in self.attendance_records:
        self.attendance_records[username] = []
        
    # Mark attendance with the current date
    from datetime import datetime
    today = datetime.now().strftime("%Y-%m-%d")
    self.attendance_records[username].append(today)
        
    # save_data(self.karyawan_data, self.attendance_records)
        
    messagebox.showinfo("Success", f"Kehadiran untuk {selected_employee['name']} telah ditandai.")
        
    #debug 
    print(f"Attendance marked for {selected_employee['name']} on {today}.")
    print("Current attendance records:", self.attendance_records)  # Debug print
        
def show_attendance(self):
    attendance_window = tk.Toplevel(self.root)
    attendance_window.title("Rekaman Kehadiran")
    attendance_window.configure(bg='#333333')
        
    tk.Label(attendance_window, text="Rekaman Kehadiran Karyawan", foreground='#ffffff' , bg='#333333').pack(pady=10)

    for emp in self.karyawan_data:
        username = emp['username']
        attendance_dates = self.attendance_records.get(username,[])
        attendance_info = f"{emp['name']} ({username}): {', '.join(attendance_dates) if attendance_dates else 'Tidak Ada Kehadiran'}"
        tk.Label(attendance_window, text=attendance_info, foreground='#ffffff' , bg='#333333').pack(pady=5)


    print("Attendace succefully showed") if attendance_info else  print("No attendance recorded for this employee")  # Debug print