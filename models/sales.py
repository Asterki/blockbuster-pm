from services.database import DatabaseService
import time


class SalesModel:
    instance = None

    def __init__(self):
        self.db = DatabaseService().get_instance()

        if SalesModel.instance is None:
            SalesModel.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = SalesModel()
        return self.instance

    def create_sale(self, movie_id, employee_id, client_id):
        sale_price = self.db.select_one('movies', '*', f'id = {movie_id}')

        return self.db.insert('sales', {
            'movie_id': movie_id,
            'employee_id': employee_id,
            'client_id': client_id,
            'sale_date': int(time.time()),
            'sale_price': sale_price[8]
        })

    def get_sale(self, _id):
        return self.db.select_one('sales', '*', f'id = {_id}')

    def get_all_sales(self):
        return self.db.select_all('sales', '*')

    def delete_sale(self, _id):
        self.db.delete('sales', f'id = {_id}')

    def update_sale(self, _id, movie_id, employee_id, client_id):
        self.db.update('sales', {
            'movie_id': movie_id,
            'employee_id': employee_id,
            'client_id': client_id
        }, f'id = {_id}')

    def get_sales_count_by_employee(self, employee_id):
        return self.db.select_all('sales', 'COUNT(*)', f'employee_id = {employee_id}')
