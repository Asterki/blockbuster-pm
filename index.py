from tkinter import *

from pages.login import LoginPage
from models.employees import UserModel

import pandas as pd
import random
import json

from models.movies import MovieModel


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
    #if input("Do you wish to preload movies? (y/n): ") == 'y':
    #    df = pd.read_csv('tmdb_5000_movies.csv')
    #    for index, row in df.iterrows():
    #        MovieModel().get_instance().create_movie(row['title'], row['overview'], row['release_date'], row['genres'],
    #                                                 row['director'], random.randint(1, 10), random.randint(1, 10),
    #                                                 random.randint(1, 10))

    LoginPage().show_window()

if __name__ == '__main__e':
    from pages.admin.movies import AdminMovies
    AdminMovies().show_window(user="admin")
