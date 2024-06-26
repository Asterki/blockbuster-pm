from datetime import datetime
from tkinter import *
from tkinter import messagebox, ttk, simpledialog

from models.employees import EmployeeModel
from services.logger import LoggerService


class AdminEmployees:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('900x600')
        self.window.attributes('-fullscreen', True)
        self.window.config(bg="#35374f")
        self.user = None

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)
            self.window.rowconfigure(i, weight=1)

        # Meny
        self.menu = Menu(self.window, bg="#535462", fg="white", activebackground="#9d9da4", activeforeground="white")
        self.menu.add_command(label='Admin Panel', command=self.go_to_admin)
        self.window.config(menu=self.menu)

        self.title = Label(self.window, text='Employees', font=('Fredoka', 25, "bold"), pady=20, fg="#d3aa1d",
                           bg="#35374f")
        self.title.grid(row=0, column=1, sticky="W")

        # Treeview that will show each employee
        self.treeview = ttk.Treeview(self.window)
        self.treeview.grid(row=1, column=1, columnspan=10, sticky="WE")
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

        # Button Actions
        self.delete_button = Button(self.window, text='Delete', command=self.delete_user, fg="white", bg="#1a1a2b",
                                    font=("Fredoka", 20, "bold"), activebackground="#23233b", activeforeground="white")
        self.delete_button.grid(row=2, column=1, columnspan=2, sticky="WE")

        self.update_button = Button(self.window, text='Update', command=self.update_user, fg="white", bg="#1a1a2b",
                                    font=("Fredoka", 20, "bold"), activebackground="#23233b", activeforeground="white")
        self.update_button.grid(row=2, column=4, columnspan=3, sticky="WE")

        self.create_button = Button(self.window, text='Create', command=self.create_user, fg="white", bg="#1a1a2b",
                                    font=("Fredoka", 20, "bold"), activebackground="#23233b", activeforeground="white")
        self.create_button.grid(row=2, column=8, columnspan=3, sticky="WE")

        self.get_and_show_users()

    def get_and_show_users(self):
        # Get all users
        users = EmployeeModel().get_instance().get_all_employees()

        # Clear current treeview
        for i in self.treeview.get_children():
            self.treeview.delete(i)

        # Put the values in the treeview
        for user in list(users):
            self.treeview.insert('', 'end', text='', values=(user[0], user[1], user[2], user[3], user[4], user[5]))

    def delete_user(self):
        # Get the current selected employee
        selected_item = self.treeview.selection()

        # If there is only one item selected
        if len(selected_item) == 1 and all(selected_item):
            user_id = self.treeview.item(selected_item[0])['values'][0]  # Get the id
            username = self.treeview.item(selected_item[0])['values'][1]  # Get the username

            if username == 'admin':  # Deleting the admin user is forbidden
                messagebox.showerror('Error', 'Cannot delete admin user')
            else:
                res = messagebox.askyesno('Delete user', f'Are you sure you want to delete {username}?')
                if res:
                    # Delete the user from the database and the treeview
                    EmployeeModel().get_instance().delete_employee(user_id)
                    self.treeview.delete(selected_item[0])

                    # Log the action
                    messagebox.showinfo('Success', 'User deleted successfully')
                    LoggerService().get_instance().log(self.user, f'Deleted user {username}')

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
        if EmployeeModel().get_instance().get_employee_by_name(username):
            messagebox.showerror('Error', 'User already exists')
        elif not username or not password or not phone_number:
            messagebox.showerror('Error', 'All fields are required')
        else:
            # Create the user
            EmployeeModel().get_instance().create_employee(username, user_created, is_admin, phone_number, password, 0)
            self.get_and_show_users()

            # Log the action
            messagebox.showinfo('Success', 'User created successfully')
            LoggerService().get_instance().log(self.user, f'Created user {username}')

    def update_user(self):
        # Get the selected item from the treeview
        selected_item = self.treeview.selection()

        if len(selected_item) == 1 and all(selected_item):  # If there is only one item selected
            user_id = self.treeview.item(selected_item[0])['values'][0]
            if self.treeview.item(selected_item[0])['values'][1] == 'admin':  # Updating the admin user is forbidden
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
                    EmployeeModel().get_instance().update_employee(user_id, new_username, new_is_admin,
                                                                   new_phone_number, new_password)
                    self.get_and_show_users()

                    # Log the action
                    messagebox.showinfo('Success', 'User updated successfully')
                    LoggerService().get_instance().log(self.user, f'Updated user {new_username}')

        elif len(selected_item) > 1 or len(selected_item) == 0:
            messagebox.showerror('Error', 'Select a user to update')

    # Navigation from here on
    def show_window(self, user):
        self.user = user
        self.window.mainloop()

    def go_to_admin(self):
        from pages.admin.index import AdminMain
        self.window.destroy()
        AdminMain().show_window(user=self.user)
