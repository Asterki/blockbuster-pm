from services.database import DatabaseService
from services.logger import LoggerService


class UserModel:
    instance = None

    def __init__(self):
        self.db = DatabaseService().get_instance()

        if UserModel.instance is None:
            UserModel.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = UserModel()
        return self.instance

    def create_user(self, name, hired_since, admin, phone_number, password, movies_sold):
        LoggerService().get_instance().log("admin", 'User created')

        return self.db.insert('employees', {
            'name': name,
            'hired_since': hired_since,
            'admin': admin,
            'phone_number': phone_number,
            'password': password,
            'movies_sold': movies_sold
        })

    def get_user(self, _id):
        return self.db.select_one('employees', '*', f'id = {_id}')

    def get_all_users(self):
        return self.db.select_all('employees', '*')

    def delete_user(self, _id):
        self.db.delete('employees', f'id = {_id}')

    def update_user(self, _id, name, hired_since, admin, phone_number, movies_sold):
        LoggerService().get_instance().log("admin", 'User updated')

        self.db.update('employees', {
            'name': name,
            'hired_since': hired_since,
            'admin': admin,
            'phone_number': phone_number,
            'movies_sold': movies_sold
        }, f'id = {_id}')

    def login(self, name, password):
        return self.db.select_one('employees', '*', f"name = '{name}' AND password = '{password}'")
