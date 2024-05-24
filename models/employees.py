from services.database import DatabaseService
from services.logger import LoggerService


class EmployeeModel:
    instance = None

    def __init__(self):
        self.db = DatabaseService().get_instance()

        if EmployeeModel.instance is None:
            EmployeeModel.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = EmployeeModel()
        return self.instance

    def create_employee(self, name, hired_since, admin, phone_number, password, movies_sold):
        LoggerService().get_instance().log("admin", 'User created')

        return self.db.insert('employees', {
            'name': name,
            'hired_since': hired_since,
            'admin': admin,
            'phone_number': phone_number,
            'password': password,
            'movies_sold': movies_sold
        })

    def get_employee(self, _id):
        return self.db.select_one('employees', '*', f'id = {_id}')

    def get_employee_by_name(self, name):
        return self.db.select_one('employees', '*', f"name = '{name}'")

    def get_all_employees(self):
        return self.db.select_all('employees', '*')

    def delete_employee(self, _id):
        self.db.delete('employees', f'id = {_id}')

    def update_employee(self, _id, name, admin, phone_number, password):
        LoggerService().get_instance().log("admin", 'User updated')

        self.db.update('employees', {
            'name': name,
            'admin': admin,
            'phone_number': phone_number,
            'password': password
        }, f'id = {_id}')

    def login(self, name, password):
        return self.db.select_one('employees', '*', f"name = '{name}' AND password = '{password}'")
