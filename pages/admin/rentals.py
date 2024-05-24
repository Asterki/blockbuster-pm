from tkinter import *
from tkinter import ttk
import time
from datetime import datetime

from services.logger import LoggerService
from services.database import DatabaseService
from models.rentals import RentalsModel
from models.clients import ClientsModel
from models.movies import MovieModel


class AdminRentals:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.attributes('-zoomed', True)
        self.window.config(bg="#35374f")
        self.user = None

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        self.menu = Menu(self.window, bg="#535462", fg="white", activebackground="#9d9da4", activeforeground="white")
        self.menu.add_command(label='Logs', command=self.go_to_logs)
        self.menu.add_command(label='Employees', command=self.go_to_employees)
        self.menu.add_command(label='Movies', command=self.go_to_employees)
        self.menu.add_command(label='Clients', command=self.go_to_clients)
        self.menu.add_command(label='Admin Panel', command=self.go_to_admin)
        self.window.config(menu=self.menu)

        Label(self.window, text='Current Rentals', font=('Fredoka', 25, "bold"), pady=20, fg="#d3aa1d", bg="#35374f").grid(row=0, column=1, columnspan=10,
                                                                            sticky="W")
        self.current_rentals = ttk.Treeview(self.window)
        self.current_rentals.grid(row=1, column=1, columnspan=10, sticky="WENS")

        self.current_rentals['columns'] = ('Rental ID', 'Movie Name', 'Rented By', 'Was sold?', 'Return time')
        self.current_rentals.column('#0', width=0, stretch=NO)
        self.current_rentals.column('Rental ID', anchor=W, width=100)
        self.current_rentals.column('Movie Name', anchor=W, width=100)
        self.current_rentals.column('Rented By', anchor=W, width=100)
        self.current_rentals.column('Was sold?', anchor=W, width=100)
        self.current_rentals.column('Return time', anchor=W, width=100)

        self.current_rentals.heading('#0', text='', anchor=W)
        self.current_rentals.heading('Rental ID', text='Rental ID', anchor=W)
        self.current_rentals.heading('Movie Name', text='Movie Name', anchor=W)
        self.current_rentals.heading('Rented By', text='Rented By', anchor=W)
        self.current_rentals.heading('Was sold?', text='Was sold?', anchor=W)
        self.current_rentals.heading('Return time', text='Return time', anchor=W)

        Label(self.window, text='Expired Rentals', font=('Fredoka', 25, "bold"), pady=20, fg="#d3aa1d", bg="#35374f").grid(row=2, column=1, columnspan=10,
                                                                            sticky="W")
        self.expired_rentals = ttk.Treeview(self.window)
        self.expired_rentals.grid(row=3, column=1, columnspan=10, sticky="WENS")

        self.expired_rentals['columns'] = ('Rental ID', 'Movie Name', 'Rented By', 'Was sold?', 'Return time')
        self.expired_rentals.column('#0', width=0, stretch=NO)
        self.expired_rentals.column('Rental ID', anchor=W, width=100)
        self.expired_rentals.column('Movie Name', anchor=W, width=100)
        self.expired_rentals.column('Rented By', anchor=W, width=100)
        self.expired_rentals.column('Was sold?', anchor=W, width=100)
        self.expired_rentals.column('Return time', anchor=W, width=100)

        self.expired_rentals.heading('#0', text='', anchor=W)
        self.expired_rentals.heading('Rental ID', text='Rental ID', anchor=W)
        self.expired_rentals.heading('Movie Name', text='Movie Name', anchor=W)
        self.expired_rentals.heading('Rented By', text='Rented By', anchor=W)
        self.expired_rentals.heading('Was sold?', text='Was sold?', anchor=W)
        self.expired_rentals.heading('Return time', text='Return time', anchor=W)

        self.get_and_show_rentals()

    def get_and_show_rentals(self):
        rentals = RentalsModel().get_all_rentals()
        for i in rentals:
            try:
                movie = MovieModel().get_movie(i[1])
                rented_by = ClientsModel().get_client(i[2])
                return_at = datetime.fromtimestamp(i[4])

                if return_at < datetime.now():
                    self.expired_rentals.insert('', 'end', text='',
                                                values=(i[0], movie[1], rented_by[1], i[5], return_at))
                else:
                    self.current_rentals.insert('', 'end', text='',
                                                values=(i[0], movie[1], rented_by[1], i[5], return_at))
            except TypeError as e:
                pass

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

    def go_to_movies(self):
        from pages.admin.movies import AdminMovies

        self.window.destroy()
        AdminMovies().show_window(user=self.user)

    def go_to_clients(self):
        from pages.admin.clients import AdminClients

        self.window.destroy()
        AdminClients().show_window(user=self.user)
