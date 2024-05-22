from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os

from services.logger import LoggerService
from services.database import DatabaseService


class AdminLogs:
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
        self.menu.add_command(label="Movies", command=self.go_to_movies)
        self.menu.add_command(label='Employees', command=self.go_to_employees)
        self.menu.add_command(label='Admin Panel', command=self.go_to_admin)
        self.menu.add_command(label="Rentals", command=self.go_to_rentals)
        self.window.config(menu=self.menu)

        self.title = Label(self.window, text='Logs', font=('Arial', 20), pady=20)
        self.title.grid(row=0, column=0, columnspan=12, sticky="WENS")

        self.treeview = ttk.Treeview(self.window)
        self.treeview.grid(row=1, column=1, columnspan=7, sticky="WENS")

        self.treeview['columns'] = ('Username', 'Action', 'Date')
        self.treeview.column('#0', width=0, stretch=NO)
        self.treeview.column('Username', anchor=W, width=100)
        self.treeview.column('Action', anchor=W, width=100)
        self.treeview.column('Date', anchor=W, width=100)

        self.treeview.heading('#0', text='', anchor=W)
        self.treeview.heading('Username', text='Username', anchor=W)
        self.treeview.heading('Action', text='Action', anchor=W)
        self.treeview.heading('Date', text='Date', anchor=W)

        self.export_button = Button(self.window, text='Export Logs', command=self.export_logs)
        self.export_button.grid(row=1, column=9, columnspan=2, sticky="WEN")

        self.get_and_show_logs()
        self.window.mainloop()

    def get_and_show_logs(self):
        logs = LoggerService().get_instance().get_logs()
        for log in list(logs):
            self.treeview.insert('', 'end', text='', values=(log[1], log[2], log[3]))

    def show_window(self, user):
        self.user = user
        self.window.mainloop()

    def export_logs(self):
        path = filedialog.askdirectory()  # Ask user to select a folder.

        if all(path):
            file_path = os.path.join(path, 'logs.xlsx')
            DatabaseService().get_instance().export_to_excel('logs', file_path)

            if os.path.exists(file_path):
                messagebox.showinfo('Success', 'Logs exported successfully')
                LoggerService().get_instance().log(self.user, 'Logs exported')
            else:
                messagebox.showerror('Error', 'Logs could not be exported')

    def go_to_admin(self):
        from pages.admin.index import AdminMain
        self.window.destroy()
        AdminMain().show_window(user=self.user)

    def go_to_movies(self):
        from pages.admin.movies import AdminMovies

        self.window.destroy()
        AdminMovies().show_window(user=self.user)

    def go_to_employees(self):
        from pages.admin.employees import AdminEmployees

        self.window.destroy()
        AdminEmployees().show_window(user=self.user)

    def go_to_rentals(self):
        from pages.admin.rentals import AdminRentals

        self.window.destroy()
        AdminRentals().show_window(user=self.user)