from tkinter import *
from PIL import Image, ImageTk, ImageOps

import os


class AdminMain:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.attributes('-zoomed', True)
        self.window.configure(bg="#35374f")
        self.user = None

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        Label(self.window, text="Admin Menu", font=('Fredoka', 25, "bold"), fg="white", bg="#35374f", pady=20).grid(
            row=0, column=0,
            columnspan=12,
            sticky="WE")

        self.image1 = Image.open(os.path.join(os.path.dirname(__file__), '../../public/images/logs_button.png'))
        self.image1 = self.image1.resize((200, 200), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.image1)
        Label(self.window, image=self.image1, font=('Fredoka', 20), fg="white", bg="#35374f").grid(row=1, column=0,
                                                                                                   columnspan=3,
                                                                                                   sticky="WE")
        Button(self.window, text='See Logs', font=('Fredoka', 15), command=self.go_to_logs).grid(row=2, column=1,
                                                                                                 columnspan=1,
                                                                                                 sticky="WE")

        self.image2 = Image.open(os.path.join(os.path.dirname(__file__), '../../public/images/employees_button.png'))
        self.image2 = self.image2.resize((200, 200), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(self.image2)
        Label(self.window, image=self.image2, font=('Fredoka', 20), fg="white", bg="#35374f").grid(row=1, column=3,
                                                                                                   columnspan=3,
                                                                                                   sticky="WE")
        Button(self.window, text='See Employees', font=('Fredoka', 15), command=self.go_to_employees).grid(row=2,
                                                                                                           column=4,
                                                                                                           columnspan=1,
                                                                                                           sticky="WE")

        self.image3 = Image.open(os.path.join(os.path.dirname(__file__), '../../public/images/movies_button.png'))
        self.image3 = self.image3.resize((200, 200), Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(self.image3)
        Label(self.window, image=self.image3, font=('Fredoka', 20), fg="white", bg="#35374f").grid(row=1, column=6,
                                                                                                   columnspan=3,
                                                                                                   sticky="WE")
        Button(self.window, text='See Movies', font=('Fredoka', 15), command=self.go_to_movies).grid(row=2, column=7,
                                                                                                     columnspan=1,
                                                                                                     sticky="WE")

        self.image4 = Image.open(os.path.join(os.path.dirname(__file__), '../../public/images/rentals_button.png'))
        self.image4 = self.image4.resize((200, 200), Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(self.image4)
        Label(self.window, image=self.image4, font=('Fredoka', 20), fg="white", bg="#35374f").grid(row=1, column=9,
                                                                                                   columnspan=3,
                                                                                                   sticky="WE")
        Button(self.window, text='See Rentals', font=('Fredoka', 15), command=self.go_to_rentals).grid(row=2, column=10,
                                                                                                       columnspan=1,
                                                                                                       sticky="WE")

        self.image5 = Image.open(os.path.join(os.path.dirname(__file__), '../../public/images/users_button.png'))
        self.image5 = self.image5.resize((200, 200), Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(self.image5)
        Label(self.window, image=self.image5, font=('Fredoka', 20), fg="white", bg="#35374f").grid(row=3, column=3,
                                                                                                   columnspan=3,
                                                                                                   sticky="WE")
        Button(self.window, text='See Clients', font=('Fredoka', 15), command=self.go_to_clients).grid(row=4, column=4,
                                                                                                       columnspan=1,
                                                                                                       sticky="WE")

        self.image6 = Image.open(os.path.join(os.path.dirname(__file__), '../../public/images/users_button.png'))
        self.image6 = self.image6.resize((200, 200), Image.ANTIALIAS)
        self.image6 = ImageTk.PhotoImage(self.image6)
        Label(self.window, image=self.image6, font=('Fredoka', 20), fg="white", bg="#35374f").grid(row=3, column=6,
                                                                                                   columnspan=3,
                                                                                                   sticky="WE")
        Button(self.window, text='See Employee Panel', font=('Fredoka', 15), command=self.go_to_employee_panel).grid(row=4,
                                                                                                              column=7,
                                                                                                              columnspan=1,
                                                                                                              sticky="WE")

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

    def go_to_clients(self):
        from pages.admin.clients import AdminClients

        self.window.destroy()
        AdminClients().show_window(user=self.user)

    def go_to_employee_panel(self):
        from pages.main import Main

        self.window.destroy()
        Main().show_window(user=self.user)
