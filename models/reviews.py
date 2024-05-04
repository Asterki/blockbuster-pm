from services.database import DatabaseService


class ReviewModel:
    def __init__(self):
        self.db = DatabaseService().get_instance()

    def create_review(self, movie_id, user_id, rating, review):
        return self.db.insert('reviews', {
            'movie_id': movie_id,
            'user_id': user_id,
            'rating': rating,
            'review': review
        })

    def get_review(self, _id):
        return self.db.select_one('reviews', '*', f'id = {_id}')

    def get_all_reviews(self):
        return self.db.select_all('reviews', '*')

    def delete_review(self, _id):
        self.db.delete('reviews', f'id = {_id}')

    def update_review(self, _id, movie_id, user_id, rating, review):
        self.db.update('reviews', {
            'movie_id': movie_id,
            'user_id': user_id,
            'rating': rating,
            'review': review
        }, f'id = {_id}')