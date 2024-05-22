from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os

from services.logger import LoggerService
from services.database import DatabaseService


class AdminRentals:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.attributes('-zoomed', True)
        self.user = None

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        self.menu = Menu(self.window)
        self.menu.add_command(label='Logs', command=self.go_to_logs)
        self.menu.add_command(label='Employees', command=self.go_to_employees)
        self.menu.add_command(label='Movies', command=self.go_to_employees)
        self.menu.add_command(label='Admin Panel', command=self.go_to_admin)
        self.window.config(menu=self.menu)

        Label(self.window, text='Current Rentals', font=('Arial', 15)).grid(row=0, column=0, columnspan=12, sticky="WENS")
        self.current_rentals = ttk.Treeview(self.window)
        self.current_rentals.grid(row=1, column=1, columnspan=10, sticky="WENS")

        self.current_rentals['columns'] = ('Movie ID', 'Movie Name', 'Rented By', 'Rented At')
        self.current_rentals.column('#0', width=0, stretch=NO)
        self.current_rentals.column('Movie ID', anchor=W, width=100)
        self.current_rentals.column('Movie Name', anchor=W, width=100)
        self.current_rentals.column('Rented By', anchor=W, width=100)
        self.current_rentals.column('Rented At', anchor=W, width=100)

        self.current_rentals.heading('#0', text='', anchor=W)
        self.current_rentals.heading('Movie ID', text='Movie ID', anchor=W)
        self.current_rentals.heading('Movie Name', text='Movie Name', anchor=W)
        self.current_rentals.heading('Rented By', text='Rented By', anchor=W)
        self.current_rentals.heading('Rented At', text='Rented At', anchor=W)

        Label(self.window, text='Expired Rentals', font=('Arial', 15)).grid(row=2, column=0, columnspan=12, sticky="WENS")
        self.expired_rentals = ttk.Treeview(self.window)
        self.expired_rentals.grid(row=3, column=1, columnspan=10, sticky="WENS")

        self.expired_rentals['columns'] = ('Movie ID', 'Movie Name', 'Rented By', 'Rented At', 'Returned At')
        self.expired_rentals.column('#0', width=0, stretch=NO)
        self.expired_rentals.column('Movie ID', anchor=W, width=100)
        self.expired_rentals.column('Movie Name', anchor=W, width=100)
        self.expired_rentals.column('Rented By', anchor=W, width=100)
        self.expired_rentals.column('Rented At', anchor=W, width=100)
        self.expired_rentals.column('Returned At', anchor=W, width=100)

        self.expired_rentals.heading('#0', text='', anchor=W)
        self.expired_rentals.heading('Movie ID', text='Movie ID', anchor=W)
        self.expired_rentals.heading('Movie Name', text='Movie Name', anchor=W)
        self.expired_rentals.heading('Rented By', text='Rented By', anchor=W)
        self.expired_rentals.heading('Rented At', text='Rented At', anchor=W)
        self.expired_rentals.heading('Returned At', text='Returned At', anchor=W)

        self.get_and_show_movies()
        self.window.mainloop()

    def get_and_show_movies(self):
        print("ejqwio")

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
