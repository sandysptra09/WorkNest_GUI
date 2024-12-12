import tkinter as tk
from tkinter import messagebox, ttk
        
def show_karyawan_interface(self):
    self.login_frame.destroy()
    self.karyawan_frame = tk.Frame(self.root)
    self.karyawan_frame.pack(pady=20)
    self.karyawan_frame.configure(bg='#333333')

    tk.Label(self.karyawan_frame, text=f"Selamat datang, {self.current_user}!", 
             foreground='#ffffff' , bg='#454545').pack(pady=10)
    
    tk.Button(self.karyawan_frame, text="Akses Profil", command=self.access_profile, 
              foreground='#ffffff' , bg='#454545').pack(pady=10)
    
    tk.Button(self.karyawan_frame, text="Keluar", command=self.root.quit, 
              foreground='#ffffff' , bg='#b90000').pack(pady=10)