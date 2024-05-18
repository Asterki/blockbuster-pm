from tkinter import *
from tkinter import messagebox

from models.users import UserModel
from services.logger import LoggerService


class LoginPage:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.resizable(False, False)

        self.label = Label(self.window, text='Login', font=('Arial', 20))
        self.label.pack()

        self.label_username = Label(self.window, text='Username', font=('Arial', 15))
        self.label_username.pack()

        self.username = StringVar()
        self.entry_username = Entry(self.window, font=('Arial', 15), textvariable=self.username)
        self.entry_username.pack()

        self.label_password = Label(self.window, text='Password', font=('Arial', 15))
        self.label_password.pack()

        self.password = StringVar()
        self.entry_password = Entry(self.window, font=('Arial', 15), show='*', textvariable=self.password)
        self.entry_password.pack()

        self.button_login = Button(self.window, text='Login', font=('Arial', 15), command=self.login)
        self.button_login.pack()

    def show_window(self):
        self.window.mainloop()

    def login(self):
        username = self.username.get()
        password = self.password.get()

        result = UserModel().get_instance().login(f'{username}', f'{password}')
        if result is None:
            messagebox.showerror('Error', 'Invalid username or password')
            self.password.set("")
        else:
            LoggerService().get_instance().log(username, 'Logged in')

            messagebox.showinfo('Success', 'Login successful')
            self.window.destroy()

            if result[3] == 'True':  # Check if the user is an admin
                from pages.admin.index import AdminMain
                AdminMain().show_window()
            else:
                from pages.main import Main as MainPage
                MainPage().show_window()
