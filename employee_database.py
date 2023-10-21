import sqlite3

class EmployeeDatabase:
    def __init__(self):
        # Создание и подключение к базе данных SQLite
        self.conn = sqlite3.connect('employee_database.db')
        self.cursor = self.conn.cursor()

        # Создание таблицы сотрудников, если она не существует
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                full_name TEXT,
                phone_number TEXT,
                email TEXT,
                salary REAL
            )
        ''')
        self.conn.commit()

    def add_employee(self, full_name, phone_number, email, salary):
        # Вставляем нового сотрудника в таблицу
        self.cursor.execute('''
            INSERT INTO employees (full_name, phone_number, email, salary)
            VALUES (?, ?, ?, ?)
        ''', (full_name, phone_number, email, salary))
        self.conn.commit()

    def update_employee(self, current_full_name, new_full_name, phone_number, email, salary):
        # Обновляем данные сотрудника в базе данных по ФИО
        if(new_full_name == ""):
            self.cursor.execute('''
                        UPDATE employees
                        SET phone_number=?, email=?, salary=?
                        WHERE full_name=?
                    ''', (phone_number, email, salary, current_full_name))
        else:
            self.cursor.execute('''
                        UPDATE employees
                        SET full_name=?, phone_number=?, email=?, salary=?
                        WHERE full_name=?
                    ''', (new_full_name, phone_number, email, salary, current_full_name))
        self.conn.commit()

    def delete_employee(self, full_name):
        # Удаляем сотрудника из базы данных по ФИО
        self.cursor.execute('DELETE FROM employees WHERE full_name=?', (full_name,))
        self.conn.commit()

    def search_employee(self, search_query):
        # Ищем сотрудников по ФИО в базе данных
        self.cursor.execute('SELECT * FROM employees WHERE full_name LIKE ?', (f'%{search_query}%',))
        result = self.cursor.fetchall()
        return result

    def display_employees(self):
        # Получаем и отображаем все записи из базы данных
        self.cursor.execute('SELECT * FROM employees')
        result = self.cursor.fetchall()
        return result

    def close(self):
        # Закрываем соединение с базой данных
        self.conn.close()