import tkinter as tk
from tkinter import messagebox
from gui.main_window import EmployeeManagementApp


if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementApp(root)
    root.mainloop()