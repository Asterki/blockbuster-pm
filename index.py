from tkinter import *

from pages.login import LoginPage
from models.employees import UserModel

import pandas as pd
import random
import json
import pyglet, os

from models.movies import MovieModel
from models.employees import UserModel

pyglet.font.add_file(os.path.join(os.path.dirname(__file__), 'public/fonts/fredoka.ttf'))


class Main:
    instance = None

    def __init__(self):
        self.current_user = None
        LoginPage().show_window()

        if Main.instance is None:
            Main.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = Main()
        return self.instance

    def set_current_user(self, user):
        self.current_user = user

    def get_current_user(self):
        return self.current_user


if __name__ == '__main__':
    if input("First time setup? (y/n): ") == 'y':
        df = pd.read_csv('tmdb_5000_movies.csv')
        for index, row in df.iterrows():
            try:
                title = row['title']
                overview = row['overview']
                release_date = row['release_date']
                genres = json.loads(row['genres'])[0]['name']
                director = json.loads(row['production_companies'])[0]['name']
                rating = random.randint(1, 10)
                price_month = random.randint(1, 10)
                price = random.randint(20, 50)
                stock = random.randint(1, 10)

                MovieModel().create_movie(title, overview, release_date, genres, director, rating, price_month, price,
                                          stock)
            except IndexError:
                pass

        UserModel().create_user('admin', 'admin', True, '321312', 'admin', 0)


    LoginPage().show_window()

if __name__ == '__main__e':
    from pages.admin.movies import AdminMovies
    AdminMovies().show_window(user="admin")
