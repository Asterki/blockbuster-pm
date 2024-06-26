import os
from tkinter import *

from PIL import Image, ImageTk


class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.attributes('-fullscreen', True)
        self.window.configure(bg="#35374f")
        self.user = None

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        # Title
        Label(self.window, text="Welcome to Blockbuster PM", font=('Fredoka', 25, "bold"), fg="white", bg="#35374f",
              pady=20).grid(
            row=0, column=0,
            columnspan=12,
            sticky="WE")

        # Button images
        self.image1 = Image.open(os.path.join(os.path.dirname(__file__), '../../public/images/sales_button.png'))
        self.image1 = self.image1.resize((200, 200), Image.LANCZOS)
        self.image1 = ImageTk.PhotoImage(self.image1)
        Label(self.window, image=self.image1, font=('Fredoka', 20), fg="white", bg="#35374f").grid(
            row=1, column=0, columnspan=3, sticky="WE")
        Button(self.window, text='New Sale', font=('Fredoka', 15), command=self.go_to_new_sale).grid(
            row=2, column=1, columnspan=1, sticky="WE")

        self.image3 = Image.open(os.path.join(os.path.dirname(__file__), '../../public/images/users_button.png'))
        self.image3 = self.image3.resize((200, 200), Image.LANCZOS)
        self.image3 = ImageTk.PhotoImage(self.image3)
        Label(self.window, image=self.image3, font=('Fredoka', 20), fg="white", bg="#35374f").grid(
            row=1, column=3, columnspan=3, sticky="WE")
        Button(self.window, text='Members', font=('Fredoka', 15), command=self.go_to_members).grid(
            row=2, column=4, columnspan=1, sticky="WE")

        self.image4 = Image.open(os.path.join(os.path.dirname(__file__), '../../public/images/rentals_button.png'))
        self.image4 = self.image4.resize((200, 200), Image.LANCZOS)
        self.image4 = ImageTk.PhotoImage(self.image4)
        Label(self.window, image=self.image4, font=('Fredoka', 20), fg="white", bg="#35374f").grid(
            row=1, column=6, columnspan=3, sticky="WE")
        Button(self.window, text='See Rentals', font=('Fredoka', 15), command=self.go_to_rentals).grid(
            row=2, column=7, columnspan=1, sticky="WE")

        self.image7 = Image.open(os.path.join(os.path.dirname(__file__), '../../public/images/logout_button.jpg'))
        self.image7 = self.image7.resize((200, 200), Image.LANCZOS)
        self.image7 = ImageTk.PhotoImage(self.image7)
        Label(self.window, image=self.image7, font=('Fredoka', 20), fg="white", bg="#35374f").grid(
            row=1, column=9, columnspan=3, sticky="WE")
        Button(self.window, text='Logout', font=('Fredoka', 15), command=self.logout).grid(
            row=2, column=10, columnspan=1, sticky="WE")

    def show_window(self, user):
        self.user = user
        self.window.mainloop()

    def logout(self):
        self.window.destroy()
        from pages.login import LoginPage
        LoginPage().show_window()

    def go_to_new_sale(self):
        self.window.destroy()
        from pages.employee.salerental import NewRentalPage
        NewRentalPage().show_page(self.user)

    def go_to_members(self):
        self.window.destroy()
        from pages.employee.members import MembersPage
        MembersPage().show_page(self.user)

    def go_to_rentals(self):
        self.window.destroy()
        from pages.employee.rentals import RentalsPage
        RentalsPage().show_page(self.user)
