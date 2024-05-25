from tkinter import *
from tkinter import messagebox, ttk, simpledialog

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
        self.menu.add_command(label='Admin Panel', command=self.go_to_admin)
        self.window.config(menu=self.menu)

        self.title = Label(self.window, text='Clients', font=('Fredoka', 25, "bold"), pady=20, fg="#d3aa1d", bg="#35374f")
        self.title.grid(row=0, column=1, sticky="W")

        self.treeview = ttk.Treeview(self.window)
        self.treeview.grid(row=1, column=1, columnspan=10, sticky="WE")
        self.treeview.bind('<Double-1>', lambda e: self.update_client())

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

        self.delete_button = Button(self.window, text='Delete', command=self.delete_client, fg="white", bg="#1a1a2b", font=("Fredoka", 20, "bold"), activebackground="#23233b", activeforeground="white")
        self.delete_button.grid(row=2, column=1, columnspan=2, sticky="WE")

        self.update_button = Button(self.window, text='Update', command=self.update_client, fg="white", bg="#1a1a2b", font=("Fredoka", 20, "bold"), activebackground="#23233b", activeforeground="white")
        self.update_button.grid(row=2, column=4, columnspan=3, sticky="WE")

        self.create_button = Button(self.window, text='Create', command=self.create_client, fg="white", bg="#1a1a2b", font=("Fredoka", 20, "bold"), activebackground="#23233b", activeforeground="white")
        self.create_button.grid(row=2, column=8, columnspan=3, sticky="WE")

        self.get_and_show_clients()
        self.window.mainloop()

    def delete_client(self):
        selected_item = self.treeview.selection()

        if len(selected_item) == 1 and all(selected_item):
            user_id = self.treeview.item(selected_item[0])['values'][0]
            name = self.treeview.item(selected_item[0])['values'][1]

            res = messagebox.askyesno('Delete user', f'Are you sure you want to delete {name}?')
            if res:
                ClientsModel().get_instance().delete_client(user_id)
                self.treeview.delete(selected_item[0])

                messagebox.showinfo('Success', 'Client deleted successfully')
                LoggerService().get_instance().log(self.user, f'Deleted client {name}')

        elif len(selected_item) > 1 or len(selected_item) == 0:
            messagebox.showerror('Error', 'Select a user to delete')

    def get_and_show_clients(self):
        clients = ClientsModel().get_all_clients()

        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for client in clients:
            self.treeview.insert('', 'end', text='', values=client)

    def create_client(self):
        name = simpledialog.askstring('Create Client', 'Enter name')
        phone_number = simpledialog.askstring('Create Client', 'Enter phone number')
        age = simpledialog.askinteger('Create Client', 'Enter age')
        address = simpledialog.askstring('Create Client', 'Enter address')
        email = simpledialog.askstring('Create Client', 'Enter email')

        if not name or not phone_number or not age or not address or not email:
            messagebox.showerror('Error', 'All fields are required')
            return

        ClientsModel().get_instance().create_client(name, phone_number, age, address, email)
        messagebox.showinfo('Success', 'Client created successfully')
        self.get_and_show_clients()
        LoggerService().get_instance().log(self.user, f'Created client {name}')

    def update_client(self):
        selected_item = self.treeview.selection()

        if len(selected_item) == 1 and all(selected_item):
            user_id = self.treeview.item(selected_item[0])['values'][0]
            name = simpledialog.askstring('Update Client', 'Enter name')
            phone_number = simpledialog.askstring('Update Client', 'Enter phone number')
            age = simpledialog.askinteger('Update Client', 'Enter age')
            banned = messagebox.askyesno('Update Client', 'Is the client banned?')
            rental_count = simpledialog.askinteger('Update Client', 'Enter the amount of rentals')
            address = simpledialog.askstring('Update Client', 'Enter address')
            email = simpledialog.askstring('Update Client', 'Enter email')

            if not name or not phone_number or not age or not address or not email:
                messagebox.showerror('Error', 'All fields are required')
                return

            ClientsModel().get_instance().update_client(user_id, name, phone_number, rental_count, banned, age, address, email)
            messagebox.showinfo('Success', 'Client updated successfully')
            self.get_and_show_clients()
            LoggerService().get_instance().log(self.user, f'Updated client {name}')

        elif len(selected_item) > 1 or len(selected_item) == 0:
            messagebox.showerror('Error', 'Select a client to update')

    # Navigation from here on
    def show_window(self, user):
        self.user = user
        self.window.mainloop()

    def go_to_admin(self):
        from pages.admin.index import AdminMain
        self.window.destroy()
        AdminMain().show_window(user=self.user)
