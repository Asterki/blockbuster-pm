from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import time

from models.clients import ClientsModel
from models.movies import MovieModel
from models.sales import SalesModel
from models.rentals import RentalsModel
from models.employees import EmployeeModel
from models.transactions import TransactionsModel

from services.logger import LoggerService


class CheckoutPage:
    def __init__(self, movie_id, client_id, type_of_sale, price, time_rented):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.configure(bg="#35374f")
        self.user = None

        self.movie_id = movie_id
        self.client_id = client_id
        self.type_of_sale = type_of_sale
        self.price = price
        self.time_rented = time_rented

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        Label(self.window, text='Checkout', font=('Fredoka', 25, "bold"), pady=20, fg="#d3aa1d",
              bg="#35374f").grid(row=0, column=1, columnspan=10, sticky="W")

        # Movie ID
        Label(self.window, text='Movie ID:', fg="white",
              bg="#35374f").grid(row=1, column=1, columnspan=1, sticky="W")
        Label(self.window, text=movie_id, fg="white",
              bg="#35374f").grid(row=1, column=2, columnspan=1, sticky="W")

        # Client ID
        Label(self.window, text='Client ID:', fg="white",
              bg="#35374f").grid(row=2, column=1, columnspan=1, sticky="W")
        Label(self.window, text=client_id, fg="white",
              bg="#35374f").grid(row=2, column=2, columnspan=1, sticky="W")

        # Type of sale
        Label(self.window, text='Rental:', fg="white",
              bg="#35374f").grid(row=3, column=1, columnspan=1, sticky="W")
        Label(self.window, text='Yes' if type_of_sale == "Rent" else 'No', fg="white",
              bg="#35374f").grid(row=3, column=2, columnspan=1, sticky="W")

        # Price
        Label(self.window, text='Total:', fg="white",
              bg="#35374f").grid(row=4, column=1, columnspan=1, sticky="W")
        Label(self.window, text=str(price if type_of_sale == "Sale" else float(price) * float(time_rented)), fg="white",
              bg="#35374f").grid(row=4, column=2, columnspan=1, sticky="W")

        # Time rented
        Label(self.window, text='Time rented:', fg="white", bg="#35374f").grid(
            row=5, column=1, columnspan=1, sticky="W")

        Label(self.window, text=f"{time_rented} Months" if type_of_sale == "Rent" else "N/A", fg="white",
              bg="#35374f").grid(row=5, column=2, columnspan=1, sticky="W")

        # Complete button
        Button(self.window, text='Confirm', command=self.confirm, bg="#d3aa1d", fg="black").grid(
            row=6, column=1, columnspan=10, sticky="WENS")

    def show_page(self, user):
        self.user = user
        self.window.mainloop()

    def confirm(self):
        # Check if there's stock of that movie
        current_movie = MovieModel().get_instance().get_movie(self.movie_id)
        if current_movie[9] == 0:
            messagebox.showerror('Error', 'Movie out of stock')
            return

        employee_id = EmployeeModel().get_instance().get_employee_by_name(self.user)[0]

        if self.type_of_sale == "Sale":
            # Create a sale
            SalesModel().get_instance().create_sale(self.movie_id, employee_id, self.client_id)

            # Create a transaction
            TransactionsModel().get_instance().create_transaction(employee_id, self.price,
                                                                  f'Sale of movie {current_movie[1]}')

            # Update stock
            MovieModel().get_instance().update_movie(self.movie_id, current_movie[1], current_movie[2],
                                                     current_movie[3], current_movie[4], current_movie[5],
                                                     current_movie[6], current_movie[7],
                                                     current_movie[8], current_movie[9] - 1)

            # Log the action
            LoggerService().get_instance().log(self.user, f'Sale of movie {self.movie_id}')
            messagebox.showinfo('Success', 'Sale completed')

            self.window.destroy()

        else:
            RentalsModel().create_rental(self.client_id, self.movie_id, int(time.time()), int(time.time()) + (int(self.time_rented) * 30 * 24 * 60 * 60))
            messagebox.showinfo('Success', 'Rental completed')
            self.window.destroy()


class NewRentalPage:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.attributes('-zoomed', True)
        self.window.configure(bg="#35374f")
        self.user = None

        self.menu = Menu(self.window, bg="#535462", fg="white", activebackground="#9d9da4", activeforeground="white")
        self.menu.add_command(label='Return to Rentals', command=self.go_to_rentals)
        self.window.config(menu=self.menu)

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        # Title
        Label(self.window, text='New Sale / Rental', font=('Fredoka', 25, "bold"), justify=CENTER, pady=20,
              fg="#d3aa1d", bg="#35374f").grid(row=0, column=1, columnspan=11, sticky="WE")

        # Movie Treeview
        Label(self.window, text='Double Click to Select a Movie', font=('Fredoka', 20, "bold"), pady=20, fg="#d3aa1d",
              bg="#35374f").grid(row=1, column=1, columnspan=10, sticky="W")
        self.treeview = ttk.Treeview(self.window)
        self.treeview.grid(row=2, column=1, columnspan=7, sticky="WENS")
        self.treeview['columns'] = ('ID', 'Name', 'Price Rent', 'Price Sale', 'Stock')

        self.treeview.column('#0', width=0, stretch=NO)
        self.treeview.column('ID', anchor=W, width=100)
        self.treeview.column('Name', anchor=W, width=100)
        self.treeview.column('Price Rent', anchor=W, width=100)
        self.treeview.column('Price Sale', anchor=W, width=100)
        self.treeview.column('Stock', anchor=W, width=100)

        self.treeview.heading('#0', text='', anchor=W)
        self.treeview.heading('ID', text='ID', anchor=W)
        self.treeview.heading('Name', text='Name', anchor=W)
        self.treeview.heading('Price Rent', text='Price Rent', anchor=W)
        self.treeview.heading('Price Sale', text='Price Sale', anchor=W)
        self.treeview.heading('Stock', text='Stock', anchor=W)

        self.get_and_show_movies()
        Button(self.window, text='Find Movie', command=self.find_movie, bg="#d3aa1d", fg="black").grid(
            row=2, column=9, columnspan=2, sticky="WENS")

        # Client Treeview
        Label(self.window, text='Double Click to Select a Client', font=('Fredoka', 20, "bold"), pady=20, fg="#d3aa1d",
              bg="#35374f").grid(row=3, column=1, columnspan=10, sticky="W")
        self.treeview2 = ttk.Treeview(self.window)
        self.treeview2.grid(row=4, column=1, columnspan=7, sticky="WENS")
        self.treeview2['columns'] = ('ID', 'Name', 'Phone', 'Banned', 'Email')

        self.treeview2.column('#0', width=0, stretch=NO)
        self.treeview2.column('ID', anchor=W, width=100)
        self.treeview2.column('Name', anchor=W, width=100)
        self.treeview2.column('Phone', anchor=W, width=100)
        self.treeview2.column('Banned', anchor=W, width=100)
        self.treeview2.column('Email', anchor=W, width=100)

        self.treeview2.heading('#0', text='', anchor=W)
        self.treeview2.heading('ID', text='ID', anchor=W)
        self.treeview2.heading('Name', text='Name', anchor=W)
        self.treeview2.heading('Phone', text='Phone', anchor=W)
        self.treeview2.heading('Banned', text='Banned', anchor=W)
        self.treeview2.heading('Email', text='Email', anchor=W)

        self.get_and_show_clients()
        Button(self.window, text='Find Client', command=self.find_client, bg="#d3aa1d", fg="black").grid(
            row=4, column=9, columnspan=2, sticky="WENS")

        # Sale configuration
        Label(self.window, text="Type of sale:", fg="white",
              bg="#35374f").grid(row=5, column=1, columnspan=1,
                                 sticky="W")
        self.type_of_sale = ttk.Combobox(self.window, values=["Rent", "Sale"], state='readonly')
        self.type_of_sale.grid(row=5, column=2, columnspan=1, sticky="WENS")

        # Time rented
        Label(self.window, text="Time rented (in months):", fg="white", bg="#35374f").grid(
            row=6, column=1, columnspan=1, sticky="W")
        self.time_rented = ttk.Combobox(self.window, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], state='readonly')
        self.time_rented.grid(row=6, column=2, columnspan=1, sticky="WENS")

        # Confirm button
        Button(self.window, text='Go to Checkout', command=self.checkout, bg="#d3aa1d", fg="black").grid(
            row=7, column=1, columnspan=10, sticky="WENS")

    def show_page(self, user):
        self.user = user
        self.window.mainloop()

    def go_to_rentals(self):
        self.window.destroy()

    def get_and_show_movies(self):
        # Get all movies and add them to the treeview
        movies = MovieModel().get_movie_count(count=100, offset=0)
        for i in movies:
            self.treeview.insert('', 'end', text='', values=(i[0], i[1], i[7], i[8], i[9]))

    def find_movie(self):
        # Ask for the movie name
        movie_name = simpledialog.askstring('Find Movie', 'Enter the movie name')
        if not movie_name:
            return

        # Get all the movies that match that name
        movies = MovieModel().find_movie(movie_name)
        if len(movies) == 0:
            messagebox.showerror('Error', 'Movies not found')
            return

        # Add it to the treeview
        self.treeview.delete(*self.treeview.get_children())
        for i in movies:
            self.treeview.insert('', 'end', text='', values=(i[0], i[1], i[7], i[8], i[9]))

    def get_and_show_clients(self):
        # Get all clients and add them to the treeview
        clients = ClientsModel().get_all_clients()
        for i in clients:
            self.treeview2.insert('', 'end', text='',
                                  values=(i[0], i[1], i[2], "Yes" if i[4] else "No", [7]))

    def find_client(self):
        # Ask for the client name
        client_name = simpledialog.askstring('Find Client', 'Enter the client name')
        if not client_name:
            return

        # Get all the clients that match that name
        clients = ClientsModel().find_client(client_name)
        if len(clients) == 0:
            messagebox.showerror('Error', 'Clients not found')
            return

        # Add it to the treeview
        self.treeview2.delete(*self.treeview2.get_children())
        for i in clients:
            self.treeview2.insert('', 'end', text='',
                                  values=(i[0], i[1], i[2], "Yes" if i[4] else "No", [7]))

    def checkout(self):
        # Get the movie_id, client_id, and type of sale
        movie_id = self.treeview.item(self.treeview.selection()[0], 'values')[0]
        client_id = self.treeview2.item(self.treeview2.selection()[0], 'values')[0]
        rental = self.type_of_sale.get()

        # Checks
        if movie_id == -1 or client_id == -1:
            messagebox.showerror('Error', 'You must select a movie and a client')
            return

        if rental == "":
            messagebox.showerror('Error', 'You must select a type of sale')
            return

        if rental == "Rent" and self.time_rented.get() == "":
            messagebox.showerror('Error', 'You must select a time rented')
            return

        # Get the price and time rented
        price = self.treeview.item(self.treeview.selection()[0], 'values')[3 if rental == "Sale" else 2]
        time_rented = self.time_rented.get()

        # Show the checkout page
        CheckoutPage(movie_id, client_id, rental, price, time_rented).show_page(self.user)
        self.window.destroy()
