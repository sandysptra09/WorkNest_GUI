import tkinter as tk
from tkinter import messagebox, ttk

def add_employee(self):
    name = self.name_entry.get()
    username = self.username_entry.get()
    password = self.password_entry.get()

    # if not all([name, username, password ]):
    #     messagebox.showerror("Error", "Semua input harus diisi!")
    #     return

    # new_employee = {
    #     'name': name,
    #     'username': username,
    #     'password': password
    # }

    # self.karyawan_data.append(new_employee)
    # save_data(self.karyawan_data, self.attendance_records)

    # self.update_employee_list()

def update_employee_list(self):
    self.employee_listbox.delete(0, tk.END)
    for emp in self.karyawan_data:
        self.employee_listbox.insert(tk.END, f"{emp['name']} ({emp['username']})")

