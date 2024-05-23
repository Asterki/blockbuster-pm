from tkinter import *


class AdminMain:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.attributes('-zoomed', True)
        self.user = None

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        Label(self.window, text='Welcome to Movie Rental Admin Centre', font=('Arial', 20)).grid(row=1,
                                                                                                 column=4,
                                                                                                 columnspan=4, pady=20,
                                                                                                 sticky="WE")

        Button(self.window, text='See Logs', font=('Arial', 15), command=self.go_to_logs).grid(row=2,
                                                                                               column=4,
                                                                                               columnspan=4,
                                                                                               sticky="WE")

        Button(self.window, text='See Users', font=('Arial', 15), command=self.go_to_employees).grid(row=3,
                                                                                                     column=4,
                                                                                                     columnspan=4,
                                                                                                     sticky="WE")

        Button(self.window, text='See Movies', font=('Arial', 15), command=self.go_to_movies).grid(row=4,
                                                                                                   column=4,
                                                                                                   columnspan=4,
                                                                                                   sticky="WE")

        Button(self.window, text='See Rentals', font=('Arial', 15), command=self.go_to_rentals).grid(row=5,
                                                                                                     column=4,
                                                                                                     columnspan=4,
                                                                                                     sticky="WE")

        self.window.mainloop()

    def show_window(self, user):
        self.user = user
        self.window.mainloop()

    def go_to_logs(self):
        from pages.admin.logs import AdminLogs

        self.window.destroy()
        AdminLogs().show_window(user=self.user)

    def go_to_employees(self):
        from pages.admin.employees import AdminEmployees

        self.window.destroy()
        AdminEmployees().show_window(user=self.user)

    def go_to_rentals(self):
        from pages.admin.rentals import AdminRentals

        self.window.destroy()
        AdminRentals().show_window(user=self.user)

    def go_to_movies(self):
        from pages.admin.movies import AdminMovies

        self.window.destroy()
        AdminMovies().show_window(user=self.user)
