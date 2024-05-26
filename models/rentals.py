from services.database import DatabaseService

from models.transactions import TransactionsModel

class RentalsModel:
    instance = None

    def __init__(self):
        self.db = DatabaseService().get_instance()

        if RentalsModel.instance is None:
            RentalsModel.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = DatabaseService()
        return self.instance

    def create_rental(self, client_id, movie_id, rental_date, return_date):
        return self.db.insert('rentals', {
            'client_id': client_id,
            'movie_id': movie_id,
            'rented_at': rental_date,
            'returned_at': return_date
        })

    def get_rental(self, _id):
        return self.db.select_one('rentals', '*', f'id = {_id}')

    def get_all_rentals(self):
        return self.db.select_all('rentals', '*')

    def delete_rental(self, _id):
        self.db.delete('rentals', f'id = {_id}')

    def update_rental(self, _id, user_id, movie_id, rental_date, return_date):
        self.db.update('rentals', {
            'user_id': user_id,
            'movie_id': movie_id,
            'rental_date': rental_date,
            'return_date': return_date
        }, f'id = {_id}')

    def get_rentals_by_user(self, user_id):
        return self.db.select_all('rentals', '*', f'user_id = {user_id}')

    def get_rentals_by_movie(self, movie_id):
        return self.db.select_all('rentals', '*', f'movie_id = {movie_id}')

    def get_rentals_by_rental_date(self, rental_date):
        return self.db.select_all('rentals', '*', f'rental_date = {rental_date}')

    def get_rentals_by_return_date(self, return_date):
        return self.db.select_all('rentals', '*', f'return_date = {return_date}')
