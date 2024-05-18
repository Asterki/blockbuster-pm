import sqlite3
import pandas as pd


class DatabaseService:
    instance = None

    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

        if DatabaseService.instance is None:
            DatabaseService.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = DatabaseService()
        return self.instance

    def create_tables(self):
        try:
            self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS employees (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            hired_since TEXT NOT NULL,
                            admin BOOLEAN NOT NULL,
                            phone_number TEXT NOT NULL,
                            movies_sold INTEGER NOT NULL,
                            password TEXT NOT NULL
                        )
                    ''')

            self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS movies (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            summary TEXT NOT NULL,
                            year INTEGER NOT NULL,
                            genre TEXT NOT NULL,
                            director TEXT NOT NULL,
                            rating INTEGER NOT NULL,
                            price_month REAL NOT NULL,
                            price REAL NOT NULL
                        )
                    ''')

            self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS clients (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            phone_number TEXT NOT NULL,
                            rentals INTEGER NOT NULL,
                            banned BOOLEAN NOT NULL
                        )
                    ''')

            self.cursor.execute('''
                         CREATE TABLE IF NOT EXISTS rentals (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            movie_id INTEGER NOT NULL,
                            user_id INTEGER NOT NULL,
                            rented_at INTEGER NOT NULL,
                            returned_at INTEGER,
                            sold BOOLEAN NOT NULL
                        )
                    ''')

            self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS inventory (
                            movie_id INTEGER NOT NULL,
                            quantity INTEGER NOT NULL
                        )
                    ''')

            self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS pro_members (
                            userid INTEGER NOT NULL,
                            since TEXT NOT NULL,
                            expires TEXT NOT NULL,
                            rentals_count INTEGER NOT NULL
                        )
                    ''')

            self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            amount REAL NOT NULL,
                            date TEXT NOT NULL
                        )
                    ''')

            self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS logs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            action TEXT NOT NULL,
                            date TEXT NOT NULL
                        )
                    ''')

            self.conn.commit()
        except Exception as e:
            print(e)

    def insert(self, table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['"' + str(value) + '"' for value in data.values()])
        try:
            self.cursor.execute(f'INSERT INTO {table} ({keys}) VALUES ({values})')
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def select_all(self, table, columns, where=None):
        columns = ', '.join(columns)
        if where:
            where = 'WHERE ' + where
        try:
            self.cursor.execute(f'SELECT {columns} FROM {table} {where}')
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return False

    def select_one(self, table, columns, where=None):
        columns = ', '.join(columns)
        if where:
            where = 'WHERE ' + where
        try:
            self.cursor.execute(f"SELECT {columns} FROM {table} {where}")
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
            return False

    def select_count(self, table, where=None, count=1, offset=0):
        if where:
            where = 'WHERE ' + where
        try:
            self.cursor.execute(f'SELECT * FROM {table} {where} LIMIT {count} OFFSET {offset}')
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return False

    def update(self, table, data, where):
        set_values = ', '.join([f'{key} = "{value}"' for key, value in data.items()])
        try:
            self.cursor.execute(f'UPDATE {table} SET {set_values} WHERE {where}')
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, table, where):
        try:
            self.cursor.execute(f'DELETE FROM {table} WHERE {where}')
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def flush(self, table):
        try:
            self.cursor.execute(f'DELETE FROM {table}')
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_headers(self, table):
        self.cursor.execute(f'PRAGMA table_info({table})')
        return [header[1] for header in self.cursor.fetchall()]

    def export_to_excel(self, table_name, file_path):
        try:
            headers = self.get_headers(table_name)
            table = self.select_all(table_name, '*')

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
                self.insert(table_name, dict(zip(headers, row)))

            return True
        except Exception as e:
            print(e)
            return False

    def close(self):
        self.conn.close()
