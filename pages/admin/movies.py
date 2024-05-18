from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os

from models.movies import MovieModel

from services.logger import LoggerService
from services.database import DatabaseService


class AdminMovies:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('800x500')
        self.window.attributes('-zoomed', True)

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)

        self.menu = Menu(self.window)
        self.menu.add_command(label="Logs", command=self.go_to_logs)
        self.menu.add_command(label='Employees', command=self.go_to_employees)
        self.menu.add_command(label='Admin Panel', command=self.go_to_admin)
        self.window.config(menu=self.menu)

        self.title = Label(self.window, text='Movies', font=('Arial', 20))
        self.title.grid(row=0, column=0, columnspan=6)

        self.treeview = ttk.Treeview(self.window)
        self.treeview.grid(row=1, column=0, columnspan=6)

        self.treeview['columns'] = ('Title', 'Overview', 'Release Date', 'Genres', 'Director', 'Rating', 'Votes',
                                    'Revenue')
        self.treeview.column('#0', width=0, stretch=NO)
        self.treeview.column('Title', anchor=W, width=200)
        self.treeview.column('Overview', anchor=W, width=300)
        self.treeview.column('Release Date', anchor=W, width=150)
        self.treeview.column('Genres', anchor=W, width=150)
        self.treeview.column('Director', anchor=W, width=150)
        self.treeview.column('Rating', anchor=W, width=50)
        self.treeview.column('Votes', anchor=W, width=50)
        self.treeview.column('Revenue', anchor=W, width=100)

        self.treeview.heading('#0', text='', anchor=W)
        self.treeview.heading('Title', text='Title', anchor=W)
        self.treeview.heading('Overview', text='Overview', anchor=W)
        self.treeview.heading('Release Date', text='Release Date', anchor=W)
        self.treeview.heading('Genres', text='Genres', anchor=W)
        self.treeview.heading('Director', text='Director', anchor=W)
        self.treeview.heading('Rating', text='Rating', anchor=W)
        self.treeview.heading('Votes', text='Votes', anchor=W)
        self.treeview.heading('Revenue', text='Revenue', anchor=W)

        self.treeview.bind("<Double-1>", self.show_movie_info)

        self.page = 0

        Button(self.window, text='Next', command=self.next_page).grid(row=2, column=1, sticky=W)
        Button(self.window, text='Previous', command=self.previous_page).grid(row=2, column=0, sticky=E)

        self.lblPage = Label(self.window, text="Page: 1")
        self.lblPage.grid(row=3, column=0, columnspan=2, sticky=NSEW)

        # Movie info
        self.lblTitle = Label(self.window, text="", font=('Arial', 20), wraplength=500, justify=CENTER)
        self.lblTitle.grid(row=4, column=0, sticky=W)

        self.lblOverview = Label(self.window, text="", font=('Arial', 15), wraplength=500, justify=CENTER)
        self.lblOverview.grid(row=5, column=0, sticky=W)

        self.lblReleaseDate = Label(self.window, text="")
        self.lblReleaseDate.grid(row=4, column=1, sticky=W)

        self.lblGenres = Label(self.window, text="")
        self.lblGenres.grid(row=5, column=1, sticky=W)

        self.lblDirector = Label(self.window, text="")
        self.lblDirector.grid(row=6, column=1, sticky=W)

        self.lblRating = Label(self.window, text="")
        self.lblRating.grid(row=7, column=1, sticky=W)

        self.lblVotes = Label(self.window, text="")
        self.lblVotes.grid(row=8, column=1, sticky=W)

        self.lblRevenue = Label(self.window, text="")
        self.lblRevenue.grid(row=9, column=1, sticky=W)

        self.get_and_show_movies()
        self.window.mainloop()

    def show_movie_info(self, event):
        selected_item = self.treeview.item(self.treeview.selection())["values"]

        self.lblTitle.config(text="Title: " + selected_item[0])
        self.lblOverview.config(text="Overview: " + selected_item[1])
        self.lblReleaseDate.config(text="Release Date: " + str(selected_item[2]))
        self.lblGenres.config(text="Genres: " + selected_item[3])
        self.lblDirector.config(text="Director: " + selected_item[4])
        self.lblRating.config(text="Rating: " + str(selected_item[5]))
        self.lblVotes.config(text="Votes: " + str(selected_item[6]))
        self.lblRevenue.config(text="Revenue: " + str(selected_item[7]))

    def get_and_show_movies(self):
        # delete current movies
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        movies = MovieModel().get_instance().get_movie_count(25, self.page*25)
        for movie in list(movies):
            self.treeview.insert('', 'end', text='', values=(movie[1], movie[2], movie[3], movie[4], movie[5], movie[6],
                                                             movie[7], movie[8]))

    def show_window(self):
        self.window.mainloop()

    def go_to_admin(self):
        from pages.admin.index import AdminMain
        self.window.destroy()
        AdminMain().show_window()

    def go_to_logs(self):
        from pages.admin.logs import AdminLogs

        self.window.destroy()
        AdminLogs().show_window()

    def go_to_employees(self):
        from pages.admin.employees import AdminEmployees

        self.window.destroy()
        AdminEmployees().show_window()

    def next_page(self):
        self.page += 1
        self.get_and_show_movies()
        self.lblPage.config(text="Page: " + str(self.page + 1))

    def previous_page(self):
        if self.page == 0:
            return
        self.page -= 1
        self.get_and_show_movies()
        self.lblPage.config(text="Page: " + str(self.page + 1))
