from tkinter import *
from tkinter import messagebox, ttk, simpledialog
from datetime import datetime

from models.clients import ClientsModel
from services.logger import LoggerService


class AdminClients:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('900x600')
        self.window.attributes('-zoomed', True)
        self.window.config(bg="#35374f")
        self.user = None

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)
            self.window.rowconfigure(i, weight=1)

        self.menu = Menu(self.window, bg="#535462", fg="white", activebackground="#9d9da4", activeforeground="white")
        self.menu.add_command(label='Logs', command=self.go_to_logs)
        self.menu.add_command(label='Movies', command=self.go_to_movies)
        self.menu.add_command(label='Rentals', command=self.go_to_rentals)
        self.menu.add_command(label='Employees', command=self.go_to_employees)
        self.menu.add_command(label='Admin Panel', command=self.go_to_admin)
        self.window.config(menu=self.menu)

        self.title = Label(self.window, text='Employees', font=('Fredoka', 25, "bold"), pady=20, fg="#d3aa1d", bg="#35374f")
        self.title.grid(row=0, column=1, sticky="W")

        self.treeview = ttk.Treeview(self.window)
        self.treeview.grid(row=1, column=1, columnspan=10, sticky="WE")
        self.treeview.bind('<Double-1>', lambda e: self.update_user())

        self.treeview['columns'] = ('ID', 'Name', 'Phone Number', 'Rental Count', 'Banned', 'Age', 'Address', 'Email')
        self.treeview.column('#0', width=0, stretch=YES)
        self.treeview.column('ID', anchor=W, width=100)
        self.treeview.column('Name', anchor=W, width=100)
        self.treeview.column('Phone Number', anchor=W, width=150)
        self.treeview.column('Rental Count', anchor=W, width=100)
        self.treeview.column('Banned', anchor=W, width=100)
        self.treeview.column('Age', anchor=W, width=100)
        self.treeview.column('Address', anchor=W, width=100)
        self.treeview.column('Email', anchor=W, width=100)

        self.treeview.heading('#0', text='', anchor=W)
        self.treeview.heading('ID', text='ID', anchor=W)
        self.treeview.heading('Name', text='Name', anchor=W)
        self.treeview.heading('Phone Number', text='Phone Number', anchor=W)
        self.treeview.heading('Rental Count', text='Rental Count', anchor=W)
        self.treeview.heading('Banned', text='Banned', anchor=W)
        self.treeview.heading('Age', text='Age', anchor=W)
        self.treeview.heading('Address', text='Address', anchor=W)
        self.treeview.heading('Email', text='Email', anchor=W)

        self.delete_button = Button(self.window, text='Delete', command=self.delete_user, fg="white", bg="#1a1a2b", font=("Fredoka", 20, "bold"), activebackground="#23233b", activeforeground="white")
        self.delete_button.grid(row=2, column=1, columnspan=2, sticky="WE")

        self.update_button = Button(self.window, text='Update', command=self.update_user, fg="white", bg="#1a1a2b", font=("Fredoka", 20, "bold"), activebackground="#23233b", activeforeground="white")
        self.update_button.grid(row=2, column=4, columnspan=3, sticky="WE")

        self.create_button = Button(self.window, text='Create', command=self.create_user, fg="white", bg="#1a1a2b", font=("Fredoka", 20, "bold"), activebackground="#23233b", activeforeground="white")
        self.create_button.grid(row=2, column=8, columnspan=3, sticky="WE")

        self.get_and_show_users()
        self.window.mainloop()

    def delete_user(self):
        pass

    def get_and_show_users(self):
        pass

    def create_user(self):
        pass

    def update_user(self):
        pass

    # Navigation from here on
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

    def go_to_movies(self):
        from pages.admin.movies import AdminMovies
        self.window.destroy()
        AdminMovies().show_window(user=self.user)

    def go_to_rentals(self):
        from pages.admin.rentals import AdminRentals
        self.window.destroy()
        AdminRentals().show_window(user=self.user)

    def go_to_employees(self):
        from pages.admin.employees import AdminEmployees
        self.window.destroy()
        AdminEmployees.show_window(user=self.user)
