import tkinter as tk
from tkinter import messagebox, ttk
from gui.widgets.employee_widgets import show_admin_interface, show_karyawan_interface
# from employee_management.controllers.dataManajemen import load_data, save_data

class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WorkNest")
        self.root.geometry("500x400")
        self.root.configure(bg='#ffffff')
        
        # self.karyawan_data, self.attendance_records = load_data()
        # print("Loaded attendance records:", self.attendance_records) #debug
        self.current_user = None
        
        
        self.login_frame = tk.Frame(self.root, bg='#ffffff', padx=20, pady=20)
        self.login_frame.pack(pady=80)
        
        tk.Label(self.login_frame, text="Username", foreground='#333', bg='#ffffff', font=("Poppins", 10, "bold")).grid(row=0, column=0, sticky="e", pady=(0,10))
        self.username_entry = tk.Entry(self.login_frame, bg='#e0e0e0', width=25, font=("Poppins", 10))
        self.username_entry.grid(row=0, column=1, pady=(0,10), padx=10)
        
        tk.Label(self.login_frame, text="Password", foreground='#333', bg='#ffffff', font=("Poppins", 10, "bold")).grid(row=1, column=0, sticky="e", pady=(0,20))
        self.password_entry = tk.Entry(self.login_frame, show='*', bg='#e0e0e0', width=25, font=("Poppins", 10))
        self.password_entry.grid(row=1, column=1, pady=(0,20), padx=10)
        
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login, bg='#2596be', fg='#ffffff', font=("Poppins", 10, "bold"), width=20)
        self.login_button.grid(row=2, columnspan=2, pady=10)
        
        self.admin_frame = None
        self.karyawan_frame = None
        self.access_profile = None
        
    def login(self):
            username = self.username_entry.get()
            password = self.password_entry.get()
            
            print(f"Attempting to login with Username: {username} and Password: {password}")
            
            if username == "admin" and password == "admin123":
                self.current_user = "admin"
                show_admin_interface(self)
            elif any(emp['username'] == username and emp['password'] == password for emp in self.karyawan_data):
                self.current_user = username
                show_karyawan_interface(self)
            else:
                messagebox.showerror("Error", "Username atau password salah.")