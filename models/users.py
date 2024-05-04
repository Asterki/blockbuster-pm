from services.database import DatabaseService


class UserModel:
    def __init__(self):
        self.db = DatabaseService().get_instance()

    def create_user(self, name, hired_since, admin, phone_number, password, movies_sold):
        try:
            self.db.cursor.execute('''
                        INSERT INTO employees (name, hired_since, admin, phone_number, password, movies_sold) 
                        VALUES (?, ?, ?, ?, ?, ?) ''', (name, hired_since, admin, phone_number, password, movies_sold))
            self.db.conn.commit()

            return True
        except Exception as e:
            print(e)
            return False

    def get_user(self, _id):
        try:
            self.db.cursor.execute('''
                        SELECT * FROM employees WHERE id = ?
                    ''', (_id,))
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
            return None

    def get_all_users(self):
        try:
            self.db.cursor.execute('''
                        SELECT * FROM employees
                    ''')
            return self.db.cursor.fetchall()
        except Exception as e:
            print(e)
            return None

    def delete_user(self, _id):
        try:
            self.db.cursor.execute('''
                        DELETE FROM employees WHERE id = ?
                    ''', (_id,))
            self.db.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update_user(self, _id, name, hired_since, admin, phone_number, movies_sold):
        try:
            self.db.cursor.execute('''
                        UPDATE employees SET name = ?, hired_since = ?, admin = ?, phone_number = ?, movies_sold = ? 
                        WHERE id = ? ''', (name, hired_since, admin, phone_number, movies_sold, _id))
            self.db.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def login(self, name, password):
        try:
            self.db.cursor.execute('''
                        SELECT * FROM employees WHERE name = ? AND password = ?
                    ''', (name, password))
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
            return None
