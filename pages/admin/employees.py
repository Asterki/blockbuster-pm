from tkinter import *
from tkinter import messagebox, ttk, simpledialog
from datetime import datetime

from models.employees import UserModel


class AdminEmployees:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('900x600')
        self.window.attributes('-zoomed', True)

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        self.menu = Menu(self.window)
        self.menu.add_command(label='Logs', command=self.go_to_logs)
        self.menu.add_command(label='Movies', command=self.go_to_movies)
        self.menu.add_command(label='Admin Panel', command=self.go_to_admin)
        self.window.config(menu=self.menu)

        self.title = Label(self.window, text='Employees', font=('Arial', 20), pady=20)
        self.title.grid(row=0, column=0, columnspan=12)

        self.treeview = ttk.Treeview(self.window)
        self.treeview.grid(row=1, column=1, columnspan=7, rowspan=6, sticky="WE")
        self.treeview.bind('<Double-1>', lambda e: self.update_user())

        self.treeview['columns'] = ('ID', 'Name', 'Hired Since', 'Is Admin', 'Phone Number', 'Movies Sold')
        self.treeview.column('#0', width=0, stretch=YES)
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

        self.delete_button = Button(self.window, text='Delete', command=self.delete_user)
        self.delete_button.grid(row=1, column=9, columnspan=2, sticky="WE")

        self.update_button = Button(self.window, text='Update', command=self.update_user)
        self.update_button.grid(row=2, column=9, columnspan=2, sticky="WE")

        self.create_button = Button(self.window, text='Create', command=self.create_user)
        self.create_button.grid(row=3, column=9, columnspan=2, sticky="WE")

        self.get_and_show_users()
        self.window.mainloop()

    def get_and_show_users(self):
        users = UserModel().get_instance().get_all_users()

        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for user in list(users):
            self.treeview.insert('', 'end', text='', values=(user[0], user[1], user[2], user[3], user[4], user[5]))

    def delete_user(self):
        selected_item = self.treeview.selection()

        if len(selected_item) == 1 and all(selected_item):
            user_id = self.treeview.item(selected_item[0])['values'][0]
            username = self.treeview.item(selected_item[0])['values'][1]

            if username == 'admin':
                messagebox.showerror('Error', 'Cannot delete admin user')
            else:
                res = messagebox.askyesno('Delete user', f'Are you sure you want to delete {username}?')
                if res:
                    UserModel().get_instance().delete_user(user_id)
                    self.treeview.delete(selected_item[0])

                    messagebox.showinfo('Success', 'User deleted successfully')

        elif len(selected_item) > 1 or len(selected_item) == 0:
            messagebox.showerror('Error', 'Select a user to delete')

    def create_user(self):
        # Get the user input
        username = simpledialog.askstring("Username", "Enter username")
        password = simpledialog.askstring("Password", "Enter password")
        phone_number = simpledialog.askstring("Phone Number", "Enter phone number")
        is_admin = messagebox.askyesno("Is Admin", "Is this user an admin?")
        user_created = datetime.now().strftime('%Y-%m-%d')

        # Verifications
        if UserModel().get_instance().get_user_by_name(username):
            messagebox.showerror('Error', 'User already exists')
        elif not username or not password or not phone_number:
            messagebox.showerror('Error', 'All fields are required')
        else:
            UserModel().get_instance().create_user(username, user_created, is_admin, phone_number, password, 0)
            messagebox.showinfo('Success', 'User created successfully')
            self.get_and_show_users()

    def update_user(self):
        selected_item = self.treeview.selection()

        if len(selected_item) == 1 and all(selected_item):
            user_id = self.treeview.item(selected_item[0])['values'][0]
            if self.treeview.item(selected_item[0])['values'][1] == 'admin':
                messagebox.showerror('Error', 'Cannot update admin user')
            else:
                # Ask for new user data
                new_username = simpledialog.askstring("Username", "Enter new username")
                new_password = simpledialog.askstring("Password", "Enter new password")
                new_phone_number = simpledialog.askstring("Phone Number", "Enter new phone number")
                new_is_admin = messagebox.askyesno("Is Admin", "Is this user an admin?")

                # Checks
                if not new_username or not new_password or not new_phone_number:
                    messagebox.showerror('Error', 'All fields are required')
                else:
                    # Update the user
                    UserModel().get_instance().update_user(user_id, new_username, new_is_admin, new_phone_number,
                                                           new_password)
                    messagebox.showinfo('Success', 'User updated successfully')

                    # Update the table
                    self.get_and_show_users()
        elif len(selected_item) > 1 or len(selected_item) == 0:
            messagebox.showerror('Error', 'Select a user to update')

    # Navigation from here on
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

    def go_to_movies(self):
        from pages.admin.movies import AdminMovies
        self.window.destroy()
        AdminMovies().show_window()
