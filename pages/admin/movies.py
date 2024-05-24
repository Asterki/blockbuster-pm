from tkinter import *
from tkinter import ttk, messagebox, simpledialog

from models.movies import MovieModel

from services.logger import LoggerService


class AdminMovies:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('800x500')
        self.window.attributes('-zoomed', True)
        self.window.config(bg="#35374f")
        self.user = None

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        self.menu = Menu(self.window, bg="#535462", fg="white", activebackground="#9d9da4", activeforeground="white")
        self.menu.add_command(label="Logs", command=self.go_to_logs)
        self.menu.add_command(label='Employees', command=self.go_to_employees)
        self.menu.add_command(label='Admin Panel', command=self.go_to_admin)
        self.menu.add_command(label="Rentals", command=self.go_to_rentals)
        self.window.config(menu=self.menu)

        self.title = Label(self.window, text='Movies', font=('Fredoka', 25, "bold"), pady=20, fg="#d3aa1d", bg="#35374f")
        self.title.grid(row=0, column=1, columnspan=10, sticky="W")

        self.treeview = ttk.Treeview(self.window)
        self.treeview.grid(row=1, column=1, columnspan=10, rowspan=6, sticky="WE")

        self.treeview['columns'] = ('ID', 'Title', 'Overview', 'Release Date', 'Genres', 'Director', 'Rating', 'Votes',
                                    'Revenue')
        self.treeview.column('#0', width=0, stretch=NO)
        self.treeview.column('ID', anchor=W, width=50)
        self.treeview.column('Title', anchor=W, width=200)
        self.treeview.column('Overview', anchor=W, width=300)
        self.treeview.column('Release Date', anchor=W, width=150)
        self.treeview.column('Genres', anchor=W, width=150)
        self.treeview.column('Director', anchor=W, width=150)
        self.treeview.column('Rating', anchor=W, width=50)
        self.treeview.column('Votes', anchor=W, width=50)
        self.treeview.column('Revenue', anchor=W, width=100)

        self.treeview.heading('#0', text='', anchor=W)
        self.treeview.heading('ID', text='ID', anchor=W)
        self.treeview.heading('Title', text='Title', anchor=W)
        self.treeview.heading('Overview', text='Overview', anchor=W)
        self.treeview.heading('Release Date', text='Release Date', anchor=W)
        self.treeview.heading('Genres', text='Genres', anchor=W)
        self.treeview.heading('Director', text='Director', anchor=W)
        self.treeview.heading('Rating', text='Rating', anchor=W)
        self.treeview.heading('Votes', text='Votes', anchor=W)
        self.treeview.heading('Revenue', text='Revenue', anchor=W)

        self.page = 0

        # Page navigation
        self.pageNavigationFrame = Frame(self.window, pady=10, padx=10, bg="#7c7d8b")
        self.pageNavigationFrame.grid(row=7, column=1, columnspan=4, sticky="WE")
        Button(self.pageNavigationFrame, text='<', command=self.previous_page, bg="#35374f", fg="white", activebackground="#3f425e", activeforeground="white").grid(row=7, column=1, sticky="WE")
        Button(self.pageNavigationFrame, text='>', command=self.next_page, bg="#35374f", fg="white", activebackground="#3f425e", activeforeground="white").grid(row=7, column=2, sticky="WE")
        self.lblPage = Label(self.pageNavigationFrame, bg="#7c7d8b", fg="white", text="Page: 1" + " Showing 25 movies per page", padx=20)
        self.lblPage.grid(row=7, column=4, sticky="WE")

        # Movie action frame
        self.movieActionFrame = Frame(self.window, pady=10, padx=10, bg="#7c7d8b")
        self.movieActionFrame.grid(row=7, column=8, columnspan=3, sticky="WE")
        Button(self.movieActionFrame, text='Update', command=self.update_movie, bg="#35374f", fg="white", activebackground="#3f425e", activeforeground="white").grid(row=7, column=7, sticky="WE")
        Button(self.movieActionFrame, text='Create', command=self.create_movie, bg="#35374f", fg="white", activebackground="#3f425e", activeforeground="white").grid(row=7, column=8, sticky="WE")
        Button(self.movieActionFrame, text='Delete', command=self.delete_movie, bg="#35374f", fg="white", activebackground="#3f425e", activeforeground="white").grid(row=7, column=9, sticky="WE")

        # Other actions
        Button(self.movieActionFrame, text="Find Movie", command=self.find_movie, bg="#35374f", fg="white", activebackground="#3f425e", activeforeground="white").grid(row=7, column=11, sticky="WE")
        Button(self.movieActionFrame, text="Reset Filter", command=self.get_and_show_movies, bg="#35374f", fg="white", activebackground="#3f425e", activeforeground="white").grid(row=7, column=12, sticky="WE")
        self.get_and_show_movies()

    def get_and_show_movies(self):
        # delete current movies
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        movies = MovieModel().get_instance().get_movie_count(25, self.page*25)
        for movie in list(movies):
            self.treeview.insert('', 'end', text='', values=(movie[0], movie[1], movie[2], movie[3], movie[4], movie[5], movie[6],
                                                             movie[7], movie[8]))

    def next_page(self):
        self.page += 1
        self.get_and_show_movies()
        self.lblPage.config(text="Page: " + str(self.page + 1) + " Showing 25 movies per page")

    def previous_page(self):
        if self.page == 0:
            return
        self.page -= 1
        self.get_and_show_movies()
        self.lblPage.config(text="Page: " + str(self.page + 1) + " Showing 25 movies per page")

    def find_movie(self):
        name = simpledialog.askstring('Find Movie', 'Enter movie name')
        if not name:
            messagebox.showerror('Error', 'Please enter a movie name')
            return

        for item in self.treeview.get_children():
            self.treeview.delete(item)

        movies = MovieModel().get_instance().find_movie(name)
        for movie in list(movies):
            self.treeview.insert('', 'end', text='', values=(movie[0], movie[1], movie[2], movie[3], movie[4], movie[5], movie[6],
                                                             movie[7], movie[8]))

    def update_movie(self):
        selected_item = self.treeview.selection()

        if not all(selected_item):
            messagebox.showerror('Error', 'Please select a movie')
            return

        movie_id = self.treeview.item(selected_item[0])['values'][0]
        name = simpledialog.askstring('Update Movie', 'Enter movie name')
        overview = simpledialog.askstring('Update Movie', 'Enter movie overview')
        release_date = simpledialog.askinteger('Update Movie', 'Enter movie release date')
        genres = simpledialog.askstring('Update Movie', 'Enter movie genres')
        director = simpledialog.askstring('Update Movie', 'Enter movie director')
        rating = simpledialog.askinteger('Update Movie', 'Enter movie rating')
        price = simpledialog.askinteger('Update Movie', 'Enter movie price')

        if not name or not overview or not release_date or not genres or not director or not rating or not price:
            messagebox.showerror('Error', 'All fields are required')
            return

        MovieModel().get_instance().update_movie(movie_id, name, overview, release_date, genres, director, rating, price)
        self.get_and_show_movies()
        messagebox.showinfo('Success', 'Movie updated successfully')

        LoggerService().get_instance().log_action(self.user, 'Updated movie', 'Movie ID: ' + str(movie_id))

    def create_movie(self):
        name = simpledialog.askstring('Create Movie', 'Enter movie name')
        overview = simpledialog.askstring('Create Movie', 'Enter movie overview')
        release_date = simpledialog.askinteger('Create Movie', 'Enter movie release date')
        genres = simpledialog.askstring('Create Movie', 'Enter movie genres')
        director = simpledialog.askstring('Create Movie', 'Enter movie director')
        rating = simpledialog.askinteger('Create Movie', 'Enter movie rating')
        price = simpledialog.askinteger('Create Movie', 'Enter movie price')

        if not name or not overview or not release_date or not genres or not director or not rating or not price:
            messagebox.showerror('Error', 'All fields are required')
            return

        MovieModel().get_instance().create_movie(name, overview, release_date, genres, director, rating, price)
        self.get_and_show_movies()
        messagebox.showinfo('Success', 'Movie created successfully')

        LoggerService().get_instance().log_action(self.user, 'Created movie', 'Movie name: ' + name)

    def delete_movie(self):
        selected_item = self.treeview.selection()

        if not all(selected_item):
            messagebox.showerror('Error', 'Please select a movie')
            return

        movie_id = self.treeview.item(selected_item[0])['values'][0]
        MovieModel().get_instance().delete_movie(movie_id)
        self.get_and_show_movies()
        messagebox.showinfo('Success', 'Movie deleted successfully')

        LoggerService().get_instance().log_action(self.user, 'Deleted movie', 'Movie ID: ' + str(movie_id))

    # Navigation
    def show_window(self, user):
        self.user = user
        self.window.mainloop()

    def go_to_admin(self):
        from pages.admin.index import AdminMain
        self.window.destroy()
        AdminMain().show_window(user=self.user)

    def go_to_logs(self):
        from pages.admin.logs import AdminLogs

        self.window.destroy()
        AdminLogs().show_window(user=self.user)

    def go_to_employees(self):
        from pages.admin.employees import AdminEmployees

        self.window.destroy()
        AdminEmployees().show_window(user=self.user)

    def go_to_rentals(self):
        from pages.admin.rentals import AdminRentals

        self.window.destroy()
        AdminRentals().show_window(user=self.user)
