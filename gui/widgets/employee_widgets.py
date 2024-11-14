
import tkinter as tk
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