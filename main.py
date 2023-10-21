import tkinter as tk

from employee_app import EmployeeApp

# pfgecr
if __name__ == '__main__':
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()

    app.db.close()