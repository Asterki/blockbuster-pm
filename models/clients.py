from services.database import DatabaseService


class ClientsModel:
    instance = None

    def __init__(self):
        self.db = DatabaseService().get_instance()

        if ClientsModel.instance is None:
            ClientsModel.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = DatabaseService()
        return self.instance

    def create_client(self, name, phone_number, age, address, email):
        return self.db.insert('clients', {
            'name': name,
            'phone_number': phone_number,
            'rental_count': 0,
            'banned': False,
            'age': age,
            'address': address,
            'email': email
        })

    def get_client(self, _id):
        return self.db.select_one('clients', '*', f'id = {_id}')

    def get_all_clients(self):
        return self.db.select_all('clients', '*')

    def delete_client(self, _id):
        self.db.delete('clients', f'id = {_id}')

    def update_client(self, _id, name, phone_number, rentals_count, banned, age, address, email):
        self.db.update('clients', {
            'name': name,
            'phone_number': phone_number,
            'rental_count': rentals_count,
            'banned': banned,
            'age': age,
            'address': address,
            'email': email
        }, f'id = {_id}')

    def find_client(self, name):
        return self.db.select_all('clients', '*', f"LOWER(name) LIKE LOWER('%{name}%');")
