import json
import os
import random

import pandas as pd
import pyglet
from tkinter import messagebox

from models.employees import EmployeeModel
from models.movies import MovieModel
from pages.login import LoginPage

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
    result = messagebox.askyesno('First time setup', 'First time setup?')

    if result:
        df = pd.read_csv('tmdb_5000_movies.csv')  # Read the csv file containing the movies
        for index, row in df.iterrows():
            try:
                # Define each variable to be added to the movie model
                title = row['title']
                overview = row['overview']
                release_date = row['release_date']
                genres = json.loads(row['genres'])[0]['name']
                director = json.loads(row['production_companies'])[0]['name']
                rating = random.randint(1, 10)
                price_month = random.randint(1, 10)
                price = random.randint(20, 50)
                stock = random.randint(1, 10)

                # Create each movie given the rows
                MovieModel().create_movie(title, overview, release_date, genres, director, rating, price_month, price,
                                          stock)
            except IndexError:
                pass

        # Create the admin user
        EmployeeModel().create_employee('admin', 'admin', True, '321312', 'admin', 0)

    # Portada
    messagebox.showinfo("Credits", "Hecho por los estudiantes de 12BTP:\nCarlos Flores\nAnny Valdez\nBirthany Vásquez\nMelvin Beltrán\nEmilio Alemán\nAngel Portillo\nOdalys Oliva\nFernando Rivera")

    LoginPage().show_window()


