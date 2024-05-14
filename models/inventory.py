from services.database import DatabaseService
import pandas as pd


class InventoryModel:
    instance = None

    def __init__(self):
        self.db = DatabaseService().get_instance()

        if InventoryModel.instance is None:
            InventoryModel.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = DatabaseService()
        return self.instance

    def update_stock(self, movie_id, stock):
        self.db.update('inventory', {'stock': stock}, f'id = {movie_id}')

    def get_stock(self, movie_id):
        return self.db.select_one('inventory', 'stock', f'id = {movie_id}')

    def get_all_movies(self):
        return self.db.select_all('inventory', '*')

    def export_to_excel(self, table_name, file_path):
        try:
            headers = self.db.get_headers(table_name)
            table = self.db.select_all(table_name, '*')

            df = pd.DataFrame(table)
            df.columns = headers
            df.to_excel(file_path, index=False)
            return df
        except Exception as e:
            print(e)
            return False

    def import_from_excel(self, table_name, file_path):
        try:
            df = pd.read_excel(file_path)
            headers = df.columns.tolist()
            data = df.values.tolist()

            for row in data:
                self.db.insert(table_name, dict(zip(headers, row)))

            return True
        except Exception as e:
            print(e)
            return False
