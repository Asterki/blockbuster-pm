from tkinter import *
from tkinter import ttk
from datetime import datetime


from models.clients import ClientsModel
from models.movies import MovieModel

from models.rentals import RentalsModel


class RentalsPage:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.attributes('-zoomed', True)
        self.window.configure(bg="#35374f")
        self.user = None

        self.menu = Menu(self.window, bg="#535462", fg="white", activebackground="#9d9da4", activeforeground="white")
        self.menu.add_command(label='Return to Panel', command=self.go_to_panel)
        self.menu.add_command(label='New Rental', command=self.new_sale)
        self.window.config(menu=self.menu)

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        # Current Rentals
        Label(self.window, text='Current Rentals', font=('Fredoka', 25, "bold"), pady=20, fg="#d3aa1d",
              bg="#35374f").grid(row=0, column=1, columnspan=10,
                                 sticky="W")
        self.current_rentals = ttk.Treeview(self.window)
        self.current_rentals.grid(row=1, column=1, columnspan=10, sticky="WENS")

        self.current_rentals['columns'] = ('Rental ID', 'Movie Name', 'Rented By', 'Return time')
        self.current_rentals.column('#0', width=0, stretch=NO)
        self.current_rentals.column('Rental ID', anchor=W, width=100)
        self.current_rentals.column('Movie Name', anchor=W, width=100)
        self.current_rentals.column('Rented By', anchor=W, width=100)
        self.current_rentals.column('Return time', anchor=W, width=100)

        self.current_rentals.heading('#0', text='', anchor=W)
        self.current_rentals.heading('Rental ID', text='Rental ID', anchor=W)
        self.current_rentals.heading('Movie Name', text='Movie Name', anchor=W)
        self.current_rentals.heading('Rented By', text='Rented By', anchor=W)
        self.current_rentals.heading('Return time', text='Return time', anchor=W)

        Button(self.window, text='Return Rental', command=self.return_existing_rental, bg="#d3aa1d", fg="black").grid(
            row=2, column=1, columnspan=10, sticky="WENS")

        # Expired Rentals
        Label(self.window, text='Expired Rentals', font=('Fredoka', 25, "bold"), pady=20, fg="#d3aa1d",
              bg="#35374f").grid(row=4, column=1, columnspan=10,sticky="W")
        self.expired_rentals = ttk.Treeview(self.window)
        self.expired_rentals.grid(row=5, column=1, columnspan=10, sticky="WENS")

        self.expired_rentals['columns'] = ('Rental ID', 'Movie Name', 'Rented By', 'Return time')
        self.expired_rentals.column('#0', width=0, stretch=NO)
        self.expired_rentals.column('Rental ID', anchor=W, width=100)
        self.expired_rentals.column('Movie Name', anchor=W, width=100)
        self.expired_rentals.column('Rented By', anchor=W, width=100)
        self.expired_rentals.column('Return time', anchor=W, width=100)

        self.expired_rentals.heading('#0', text='', anchor=W)
        self.expired_rentals.heading('Rental ID', text='Rental ID', anchor=W)
        self.expired_rentals.heading('Movie Name', text='Movie Name', anchor=W)
        self.expired_rentals.heading('Rented By', text='Rented By', anchor=W)
        self.expired_rentals.heading('Return time', text='Return time', anchor=W)

        Button(self.window, text='Return Rental', command=self.return_expired_rental, bg="#d3aa1d", fg="black").grid(
            row=6, column=1, columnspan=10, sticky="WENS")

        self.get_and_show_rentals()

    def get_and_show_rentals(self):
        rentals = RentalsModel().get_all_rentals()
        for i in rentals:
            try:
                movie = MovieModel().get_movie(i[1])
                rented_by = ClientsModel().get_client(i[2])
                return_at = datetime.fromtimestamp(i[4])

                if return_at < datetime.now():
                    self.expired_rentals.insert('', 'end', text='',
                                                values=(i[0], movie[1], rented_by[1], return_at))
                else:
                    self.current_rentals.insert('', 'end', text='',
                                                values=(i[0], movie[1], rented_by[1], return_at))
            except TypeError as e:
                pass

    def return_existing_rental(self):
        rental = self.current_rentals.selection()

        if rental:
            RentalsModel().return_rental(rental[0])
            self.current_rentals.delete(rental)


    def return_expired_rental(self):
        rental = self.expired_rentals.selection()



    def show_page(self, user):
        self.user = user
        self.window.mainloop()

    def go_to_panel(self):
        from pages.employee.index import Main
        self.window.destroy()
        Main().show_window(user=self.user)

    def new_sale(self):
        from pages.employee.salerental import NewRentalPage
        self.window.destroy()
        NewRentalPage().show_page(user=self.user)

    def check_sale(self):
        pass
