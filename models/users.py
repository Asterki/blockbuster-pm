from services.database import DatabaseService


class UserModel:
    def __init__(self):
        self.db = DatabaseService().get_instance()

    def create_user(self, name, hired_since, admin, phone_number, password, movies_sold):
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
        self.db.update('employees', {
            'name': name,
            'hired_since': hired_since,
            'admin': admin,
            'phone_number': phone_number,
            'movies_sold': movies_sold
        }, f'id = {_id}')

    def login(self, name, password):
        return self.db.select_one('employees', '*', f'name = "{name}" AND password = "{password}"')