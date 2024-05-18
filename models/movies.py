from services.database import DatabaseService


class MovieModel:
    instance = None

    def __init__(self):
        self.db = DatabaseService().get_instance()

        if MovieModel.instance is None:
            MovieModel.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = DatabaseService()
        return self.instance

    def create_movie(self, title, summary, year, genre, director, rating, price_month, price):
        return self.db.insert('movies', {
            'title': title,
            'summary': summary,
            'year': year,
            'genre': genre,
            'director': director,
            'rating': rating,
            'price_month': price_month,
            'price': price
        })

    def get_movie(self, _id):
        return self.db.select_one('movies', '*', f'id = {_id}')

    def get_all_movies(self):
        return self.db.select_all('movies', '*')

    def delete_movie(self, _id):
        self.db.delete('movies', f'id = {_id}')

    def update_movie(self, _id, title, summary, year, genre, director, rating, price_month, price):
        self.db.update('movies', {
            'title': title,
            'summary': summary,
            'year': year,
            'genre': genre,
            'director': director,
            'rating': rating,
            'price_month': price_month,
            'price': price
        }, f'id = {_id}')

    def get_movies_by_genre(self, genre):
        return self.db.select_all('movies', '*', f'genre = {genre}')

    def get_movies_by_director(self, director):
        return self.db.select_all('movies', '*', f'director = {director}')

    def get_movies_by_rating(self, rating):
        return self.db.select_all('movies', '*', f'rating = {rating}')

    def get_movies_by_price(self, price):
        return self.db.select_all('movies', '*', f'price = {price}')

    def get_movies_by_price_month(self, price_month):
        return self.db.select_all('movies', '*', f'price_month = {price_month}')

    def get_movies_by_year(self, year):
        return self.db.select_all('movies', '*', f'year = {year}')

    def get_movie_count(self, count, offset):
        return self.db.select_count('movies', count=count, offset=offset)
