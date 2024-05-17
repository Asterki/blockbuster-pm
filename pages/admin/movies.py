from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os

from services.logger import LoggerService
from services.database import DatabaseService


class AdminMovies:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.resizable(False, False)

        self.menu = Menu(self.window)
        self.menu.add_command(label="Logs", command=self.go_to_logs)
        self.menu.add_command(label='Employees', command=self.go_to_employees)
        self.menu.add_command(label='Admin Panel', command=self.go_to_admin)
        self.window.config(menu=self.menu)

        self.treeview = ttk.Treeview(self.window)
        self.treeview.pack()

        self.treeview['columns'] = ('Title', 'Overview', 'Release Date', 'Genres', 'Director', 'Rating', 'Votes',
                                      'Revenue')
        self.treeview.column('#0', width=0, stretch=NO)
        self.treeview.column('Title', anchor=W, width=100)
        self.treeview.column('Overview', anchor=W, width=100)
        self.treeview.column('Release Date', anchor=W, width=100)
        self.treeview.column('Genres', anchor=W, width=100)
        self.treeview.column('Director', anchor=W, width=100)
        self.treeview.column('Rating', anchor=W, width=100)
        self.treeview.column('Votes', anchor=W, width=100)
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

        self.button = Button(self.window, text='Go Back', font=('Arial', 15), command=self.go_to_admin)
        self.button.pack()

        self.get_and_show_movies()
        self.window.mainloop()

    def get_and_show_movies(self):
        logs = LoggerService().get_instance().get_logs()
        for log in list(logs):
            self.treeview.insert('', 'end', text='', values=(log[1], log[2], log[3]))

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
