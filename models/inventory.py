from services.database import DatabaseService


class InventoryModel:
    def __init__(self):
        self.db = DatabaseService().get_instance()

    def update_stock(self, movie_id, stock):
        self.db.update('inventory', {'stock': stock}, f'id = {movie_id}')

    def get_stock(self, movie_id):
        return self.db.select_one('inventory', 'stock', f'id = {movie_id}')

    def get_all_movies(self):
        return self.db.select_all('inventory', '*')
