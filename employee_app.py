import tkinter as tk
from tkinter import ttk

from employee_database import EmployeeDatabase

class EmployeeApp:
    def __init__(self, root):
        self.search_entry = None
        self.entry_salary = None
        self.entry_email = None
        self.entry_phone_number = None
        self.entry_full_name = None
        self.search_label = None
        self.label_salary = None
        self.label_email = None
        self.label_full_name = None
        self.label_phone_number = None
        self.root = root
        self.root.title('Список сотрудников компании')
        self.db = EmployeeDatabase()

        self.create_gui()

    def create_gui(self):
        # Создание элементов интерфейса Tkinter
        self.label_full_name = tk.Label(self.root, text='ФИО:')
        self.label_phone_number = tk.Label(self.root, text='Номер телефона:')
        self.label_email = tk.Label(self.root, text='Адрес электронной почты:')
        self.label_salary = tk.Label(self.root, text='Заработная плата:')
        self.search_label = tk.Label(self.root, text='Поиск/удаление/изменение по ФИО:')

        self.entry_full_name = tk.Entry(self.root)
        self.entry_phone_number = tk.Entry(self.root)
        self.entry_email = tk.Entry(self.root)
        self.entry_salary = tk.Entry(self.root)
        self.search_entry = tk.Entry(self.root)

        button_add = tk.Button(self.root, text='Добавить сотрудника', command=self.add_employee)
        button_update = tk.Button(self.root, text='Изменить сотрудника', command=self.update_employee)
        button_delete = tk.Button(self.root, text='Удалить сотрудника', command=self.delete_employee)
        button_search = tk.Button(self.root, text='Поиск', command=self.search_employee)

        self.tree = ttk.Treeview(self.root, columns=('ID', 'ФИО', 'Номер телефона', 'Адрес электронной почты', 'Заработная плата'))
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='ФИО')
        self.tree.heading('#3', text='Номер телефона')
        self.tree.heading('#4', text='Адрес электронной почты')
        self.tree.heading('#5', text='Заработная плата, тыс. р.')

        # Расположение элементов на форме
        self.label_full_name.grid(row=0, column=0, padx=5, pady=5)
        self.label_phone_number.grid(row=1, column=0, padx=5, pady=5)
        self.label_email.grid(row=2, column=0, padx=5, pady=5)
        self.label_salary.grid(row=3, column=0, padx=5, pady=5)
        self.search_label.grid(row=6, column=0, padx=5, pady=5)

        self.entry_full_name.grid(row=0, column=1, padx=5, pady=5)
        self.entry_phone_number.grid(row=1, column=1, padx=5, pady=5)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)
        self.entry_salary.grid(row=3, column=1, padx=5, pady=5)
        self.search_entry.grid(row=6, column=1, padx=5, pady=5)

        button_add.grid(row=4, column=0, columnspan=1, padx=5, pady=5)
        button_update.grid(row=4, column=1, columnspan=1, padx=5, pady=5)
        button_delete.grid(row=4, column=2, columnspan=1, padx=5, pady=5)
        button_search.grid(row=6, column=2, padx=5, pady=5)

        self.tree.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

        # Отображение записей из базы данных
        self.display_employees()

    def add_employee(self):
        """ Добавление сотрудника по ФИО"""
        full_name = self.entry_full_name.get()
        if full_name == "":
            return
        phone_number = self.entry_phone_number.get()
        email = self.entry_email.get()
        salary = self.entry_salary.get()
        self.db.add_employee(full_name, phone_number, email, salary)
        self.clear_entries()
        self.display_employees()

    def update_employee(self):
        """ Обновление сотрудника по ФИО"""
        current_full_name = self.search_entry.get()
        new_full_name = self.entry_full_name.get()
        phone_number = self.entry_phone_number.get()
        email = self.entry_email.get()
        salary = self.entry_salary.get()
        self.db.update_employee(current_full_name, new_full_name, phone_number, email, salary)
        self.clear_entries()
        self.display_employees()

    def delete_employee(self):
        """ Удаление сотрудника по ФИО"""
        full_name = self.search_entry.get()
        self.db.delete_employee(full_name)
        self.clear_entries()
        self.display_employees()

    def search_employee(self):
        """ Поиск сотрудника по ФИО"""
        search_query = self.search_entry.get()
        result = self.db.search_employee(search_query)
        self.tree.delete(*self.tree.get_children())
        for row in result:
            self.tree.insert('', 'end', values=row)

    def display_employees(self):
        """ Отображение записей из базы данных """
        result = self.db.display_employees()
        self.tree.delete(*self.tree.get_children())
        for row in result:
            self.tree.insert('', 'end', values=row)

    def clear_entries(self):
        """ Очистка полей для ФИО, почты, телефона и зп """
        self.entry_full_name.delete(0, 'end')
        self.entry_phone_number.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_salary.delete(0, 'end')