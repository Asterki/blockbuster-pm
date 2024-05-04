from services.database import DatabaseService


class StockModel:
    def __init__(self):
        self.db = DatabaseService().get_instance()

    def create_stock(self, name, price, stock):