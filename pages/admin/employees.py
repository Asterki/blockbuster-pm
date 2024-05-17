from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from models.users import UserModel


class AdminEmployees:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('900x600')
        self.window.resizable(False, False)

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)

        self.treeview = ttk.Treeview(self.window)
        self.treeview.grid(row=0, column=0, columnspan=1, rowspan=6)

        self.treeview['columns'] = ('ID', 'Name', 'Hired Since', 'Is Admin', 'Phone Number', 'Movies Sold')
        self.treeview.column('#0', width=0, stretch=NO)
        self.treeview.column('ID', anchor=W, width=100)
        self.treeview.column('Name', anchor=W, width=100)
        self.treeview.column('Hired Since', anchor=W, width=150)
        self.treeview.column('Is Admin', anchor=W, width=100)
        self.treeview.column('Phone Number', anchor=W, width=150)
        self.treeview.column('Movies Sold', anchor=W, width=150)

        self.treeview.heading('#0', text='', anchor=W)
        self.treeview.heading('ID', text='ID', anchor=W)
        self.treeview.heading('Name', text='Name', anchor=W)
        self.treeview.heading('Hired Since', text='Hired Since', anchor=W)
        self.treeview.heading('Is Admin', text='Is Admin', anchor=W)
        self.treeview.heading('Phone Number', text='Phone Number', anchor=W)
        self.treeview.heading('Movies Sold', text='Movies Sold', anchor=W)

        self.button = Button(self.window, text='Go Back', font=('Arial', 15), command=self.go_back)
        self.button.grid(row=0, column=1, columnspan=1)

        self.delete_button = Button(self.window, text='Delete', font=('Arial', 15), command=self.delete_user)
        self.delete_button.grid(row=1, column=1, columnspan=1)

        self.update_button = Button(self.window, text='Update', font=('Arial', 15), command=self.update_user)
        self.update_button.grid(row=2, column=1, columnspan=1)

        self.get_and_show_users()
        self.window.mainloop()

    def get_and_show_users(self):
        users = UserModel().get_instance().get_all_users()
        print(users)
        for user in list(users):
            self.treeview.insert('', 'end', text='', values=(user[0], user[1], user[2], user[3], user[4], user[5]))

    def delete_user(self):
        selected_item = self.treeview.selection()
        user_id = self.treeview.item(selected_item)['values'][0]
        username = self.treeview.item(selected_item)['values'][1]

        if username == 'admin':
            messagebox.showerror('Error', 'Cannot delete admin user')
        else:
            res = messagebox.askyesno('Delete user', f'Are you sure you want to delete {username}?')
            if res:
                UserModel().get_instance().delete_user(user_id)
                self.treeview.delete(selected_item)

                messagebox.showinfo('Success', 'User deleted successfully')

    def update_user(self):
        selected_item = self.treeview.selection()
        user_id = self.treeview.item(selected_item)['values'][0]
        UserModel().get_instance().update_user(user_id, 'name', '2021-01-01', True, '123456789', 0)
        self.treeview.delete(selected_item)
        self.get_and_show_users()

    def show_window(self):
        self.window.mainloop()

    def go_back(self):
        from pages.admin.index import AdminMain
        self.window.destroy()
        AdminMain().show_window()
