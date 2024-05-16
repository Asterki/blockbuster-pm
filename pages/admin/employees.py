from tkinter import *
from tkinter import ttk

from models.users import UserModel


class AdminEmployees:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('600x600')
        self.window.resizable(False, False)

        self.treeview = ttk.Treeview(self.window)
        self.treeview.pack()

        self.treeview['columns'] = ('ID', 'Name', 'Hired Since', 'Is Admin', 'Phone Number', 'Movies Sold')
        self.treeview.column('#0', width=0, stretch=NO)
        self.treeview.column('ID', anchor=W, width=100)
        self.treeview.column('Name', anchor=W, width=100)
        self.treeview.column('Hired Since', anchor=W, width=100)
        self.treeview.column('Is Admin', anchor=W, width=100)
        self.treeview.column('Phone Number', anchor=W, width=100)
        self.treeview.column('Movies Sold', anchor=W, width=100)

        self.treeview.heading('#0', text='', anchor=W)
        self.treeview.heading('ID', text='ID', anchor=W)
        self.treeview.heading('Name', text='Name', anchor=W)
        self.treeview.heading('Hired Since', text='Hired Since', anchor=W)
        self.treeview.heading('Is Admin', text='Is Admin', anchor=W)
        self.treeview.heading('Phone Number', text='Phone Number', anchor=W)
        self.treeview.heading('Movies Sold', text='Movies Sold', anchor=W)

        self.button = Button(self.window, text='Go Back', font=('Arial', 15), command=self.go_back)
        self.button.pack()

        self.get_and_show_users()
        self.window.mainloop()

    def get_and_show_users(self):
        users = UserModel().get_instance().get_all_users()
        print(users)
        for user in list(users):
            self.treeview.insert(parent='', index=0, iid=0, text='', values=(user[0], user[1], user[2], user[3], user[4], user[5]))

    def show_window(self):
        self.window.mainloop()

    def go_back(self):
        from pages.admin.index import AdminMain
        self.window.destroy()
        AdminMain().show_window()
