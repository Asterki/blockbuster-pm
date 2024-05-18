from tkinter import *


class AdminMain:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.resizable(False, False)

        self.label = Label(self.window, text='Welcome to Movie Rental Admin Centre', font=('Arial', 20))
        self.label.pack()

        self.button = Button(self.window, text='See Logs', font=('Arial', 15), command=self.go_to_logs)
        self.button.pack()

        self.button = Button(self.window, text='See Users', font=('Arial', 15), command=self.go_to_employees)
        self.button.pack()

        self.button = Button(self.window, text='See Movies', font=('Arial', 15), command=self.go_to_movies)
        self.button.pack()

        self.button = Button(self.window, text='See Rentals', font=('Arial', 15), command=self.go_to_rentals)
        self.button.pack()

        self.window.mainloop()

    def show_window(self):
        self.window.mainloop()

    def go_to_logs(self):
        from pages.admin.logs import AdminLogs

        self.window.destroy()
        AdminLogs().show_window()

    def go_to_employees(self):
        from pages.admin.employees import AdminEmployees

        self.window.destroy()
        AdminEmployees().show_window()

    def go_to_rentals(self):
        from pages.admin.rentals import AdminRentals

        self.window.destroy()
        AdminRentals().show_window()

    def go_to_movies(self):
        from pages.admin.movies import AdminMovies

        self.window.destroy()
        AdminMovies().show_window()