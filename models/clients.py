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

    def create_client(self, name, phone_number, rentals):
        return self.db.insert('clients', {
            'name': name,
            'phone_number': phone_number,
            'rentals': rentals
        })

    def get_client(self, _id):
        return self.db.select_one('clients', '*', f'id = {_id}')

    def get_all_clients(self):
        return self.db.select_all('clients', '*')

    def delete_client(self, _id):
        self.db.delete('clients', f'id = {_id}')

    def update_client(self, _id, name, phone_number, rentals):
        self.db.update('clients', {
            'name': name,
            'phone_number': phone_number,
            'rentals': rentals
        }, f'id = {_id}')
