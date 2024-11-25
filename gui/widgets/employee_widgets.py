import tkinter as tk
from tkinter import messagebox, ttk
        
def show_admin_interface(self):
        self.login_frame.destroy()
        self.admin_frame = tk.Frame(self.root, bg='#ffffff', padx=50, pady=50)
        self.admin_frame.pack(pady=20)
        self.admin_frame.configure(bg='#ffffff')
        
        tk.Button(
            self.admin_frame, text="Manajemen Data Karyawan", 
            command=self.manage_employees, 
            foreground='#ffffff', bg='#2596be', 
            font=("Poppins", 10, "bold"),
            width=25, pady=10
        ).pack(pady=(0, 10))

        tk.Button(
            self.admin_frame, text="Pelacak Kehadiran Karyawan", 
            command=self.employee_tracking, 
            foreground='#ffffff', bg='#2596be', 
            font=("Poppins", 10, "bold"),
            width=25, pady=10
        ).pack(pady=(0, 10))
        
        tk.Button(
            self.admin_frame, text="Keluar", 
            command=self.root.quit, 
            foreground='#ffffff', bg='#b90000', 
            font=("Poppins", 10, "bold"),
            width=25, pady=10
        ).pack(pady=(0, 10))

def show_karyawan_interface(self):
    self.login_frame.destroy()
    self.karyawan_frame = tk.Frame(self.root)
    self.karyawan_frame.pack(pady=20)
    self.karyawan_frame.configure(bg='#333333')

    tk.Label(self.karyawan_frame, text=f"Selamat datang, {self.current_user}!", foreground='#ffffff' , bg='#454545').pack(pady=10)
    tk.Button(self.karyawan_frame, text="Akses Profil", command=self.access_profile, foreground='#ffffff' , bg='#454545').pack(pady=10)
    tk.Button(self.karyawan_frame, text="Keluar", command=self.root.quit, foreground='#ffffff' , bg='#b90000').pack(pady=10)
    
def go_back_to_admin1(self): # go back for "manage employees"
    self.manage_frame.destroy()
    self.show_admin_interface()
    
def go_back_to_admin2(self): # go back for "tracking  employees"

    self.tracking_frame.destroy()
    self.show_admin_interface()
        

def add_employee(self):
    name = self.name_entry.get()
    username = self.username_entry.get()
    password = self.password_entry.get()

    if not all([name, username, password ]):
        messagebox.showerror("Error", "Semua input harus diisi!")
        return

    new_employee = {
        'name': name,
        'username': username,
        'password': password
    }

    self.karyawan_data.append(new_employee)
    # save_data(self.karyawan_data, self.attendance_records)

    self.update_employee_list()

def update_employee_list(self):
    self.employee_listbox.delete(0, tk.END)
    for emp in self.karyawan_data:
        self.employee_listbox.insert(tk.END, f"{emp['name']} ({emp['username']})")

def employee_tracking(self):
    self.admin_frame.destroy()
    self.tracking_frame = tk.Frame(self.root)
    self.tracking_frame.pack(pady=20)
    self.tracking_frame.configure(bg='#333333')
        
    tk.Label(self.tracking_frame, text="Pelacak Kehadiran Karyawan", foreground='#ffffff' , bg='#333333').grid(row=0, columnspan=2)
        
    self.employee_listbox = tk.Listbox(self.tracking_frame, width=50, foreground='#ffffff' , bg='#454545')
    self.employee_listbox.grid(row=2, columnspan=2, pady=20)
        
    for emp in self.karyawan_data:
        self.employee_listbox.insert(tk.END, f"{emp['name']} ({emp['username']})")

    tk.Button(self.tracking_frame, text="Tandai Kehadiran", command=self.mark_attendance, foreground='#ffffff' , bg='#454545').grid(row=3, columnspan=2)
    tk.Button(self.tracking_frame, text="Tampilkan Kehadiran", command=self.show_attendance, foreground='#ffffff' , bg='#454545').grid(row=5, columnspan=2)
    tk.Button(self.tracking_frame, text="Kembali", command=self.go_back_to_admin2, foreground='#ffffff' , bg='#b90000').grid(row=7, columnspan=2)
        
    names = [emp['name'] for emp in self.karyawan_data]
    ttk.Combobox(self.tracking_frame, values=names).grid(row=9, columnspan=2)

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