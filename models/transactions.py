import time

from services.database import DatabaseService


class TransactionsModel:
    instance = None

    def __init__(self):
        self.db = DatabaseService().get_instance()

        if TransactionsModel.instance is None:
            TransactionsModel.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = TransactionsModel()
        return self.instance

    def create_transaction(self, employee_id, amount, description):
        return self.db.insert('transactions', {
            'user_id': employee_id,
            'amount': amount,
            'description': description,
            'date': time.strftime('%Y-%m-%d %H:%M:%S')
        })
