from tkinter import *

from pages.login import LoginPage
from pages.admin.employees import AdminEmployees
from models.users import UserModel


class Main:
    instance = None

    def __init__(self):
        self.current_user = None
        LoginPage().show_window()

        if Main.instance is None:
            Main.instance = self

    def get_instance(self):
        if self.instance is None:
            self.instance = Main()
        return self.instance

    def set_current_user(self, user):
        self.current_user = user

    def get_current_user(self):
        return self.current_user


if __name__ == '__main__':
    # UserModel().get_instance().create_user('adm23in', '2021-01-01', True, '123456789', 'adm23in', 0)
    AdminEmployees().show_window()
