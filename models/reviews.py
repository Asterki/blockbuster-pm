from services.database import DatabaseService


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

    def create_review(self, user_id, movie_id, rating, review):
        return self.db.insert('reviews', {
            'user_id': user_id,
            'movie_id': movie_id,
            'rating': rating,
            'review': review
        })

    def get_review(self, _id):
        return self.db.select_one('reviews', '*', f'id = {_id}')

    def get_all_reviews(self):
        return self.db.select_all('reviews', '*')

    def delete_review(self, _id):
        self.db.delete('reviews', f'id = {_id}')

    def update_review(self, _id, user_id, movie_id, rating, review):
        self.db.update('reviews', {
            'user_id': user_id,
            'movie_id': movie_id,
            'rating': rating,
            'review': review
        }, f'id = {_id}')

    def get_reviews_by_user(self, user_id):
        return self.db.select_all('reviews', '*', f'user_id = {user_id}')

    def get_reviews_by_movie(self, movie_id, rating=None):
        return self.db.select_all('reviews', '*', f'movie_id = {movie_id} AND rating = {rating}')


