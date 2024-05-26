from datetime import datetime

from services.database import DatabaseService


class LoggerService:
    instance = None

    def __init__(self):
        self.db = DatabaseService().get_instance()

        if LoggerService.instance is None:
            LoggerService.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = LoggerService()
        return self.instance

    def log(self, user_id, action):
        return self.db.insert('logs', {
            'user_id': user_id,
            'action': action,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    def get_logs(self):
        return self.db.select_all('logs', '*')

    def get_logs_by_user(self, user_id):
        return self.db.select('logs', '*', {'user_id': user_id})

    def delete_logs(self):
        return self.db.delete_all('logs')
