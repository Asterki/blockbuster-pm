import os
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

from definitions import ROOT_DIR
from models.employees import EmployeeModel
from services.logger import LoggerService


class LoginPage:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.resizable(False, False)
        self.window.config(bg="#35374f")

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        # Title
        self.label = Label(self.window, text='Login', font=('Fredoka', 25, "bold"), fg="white", bg="#35374f")
        self.label.grid(row=0, column=0, columnspan=12, sticky="WENS")

        # Image
        self.image = Image.open(os.path.join(ROOT_DIR, './public/images/user.png'))
        self.image = self.image.resize((100, 100), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)
        Label(self.window, image=self.image, bg="#35374f").grid(row=1, column=5, columnspan=2, sticky="WENS")

        # Label for the username input
        self.label_username = Label(self.window, text='Username', font=('Arial', 15, "bold"), fg="white", bg="#35374f")
        self.label_username.grid(row=2, column=0, columnspan=12, sticky="WENS")

        # Username input
        self.username = StringVar()
        self.entry_username = Entry(self.window, font=('Fredoka', 15), textvariable=self.username, fg="white",
                                    bg="#35374f")
        self.entry_username.grid(row=3, column=2, columnspan=8, sticky="WENS")

        # Label for the password input
        self.label_password = Label(self.window, text='Password', font=('Fredoka', 15, "bold"), fg="white", bg="#35374f")
        self.label_password.grid(row=4, column=0, columnspan=12, sticky="WENS")

        # Password input
        self.password = StringVar()
        self.entry_password = Entry(self.window, font=('Fredoka', 15), show='*', textvariable=self.password, fg="white",
                                    bg="#35374f")
        self.entry_password.grid(row=5, column=2, columnspan=8, sticky="WENS")

        # This is just to add some padding
        Label(text="", bg="#35374f").grid(row=6, column=0, columnspan=12, sticky="WENS")

        # Login button
        self.button_login = Button(self.window, text='Login', font=('Fredoka', 15, "bold"), command=self.login, bg="#fac710",
                                   fg="white")
        self.button_login.grid(row=7, column=2, columnspan=8, sticky="WENS")

    def show_window(self):
        self.window.mainloop()

    def login(self):
        # Get the values from the entries
        username = self.username.get()
        password = self.password.get()

        # Authenticate the user
        result = EmployeeModel().get_instance().login(f'{username}', f'{password}')
        if result is None:  # If no user is returned, then invalid credentials
            messagebox.showerror('Error', 'Invalid username or password')
            self.password.set("")
        else:
            # Log the action
            LoggerService().get_instance().log(username, 'Logged in')

            # Destroy the window
            messagebox.showinfo('Success', 'Login successful')
            self.window.destroy()

            # Move to the corresponding page, given if the user is an admin or not
            if result[3] == 'True':  # Check if the user is an admin
                from pages.admin.index import AdminMain
                AdminMain().show_window(user=result[1])
            else:
                from pages.employee.index import Main as MainPage
                MainPage().show_window(user=result[1])
