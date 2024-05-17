from tkinter import *

from pages.login import LoginPage
from pages.admin.employees import AdminEmployees
from models.users import UserModel


class Main:
    def __init__(self):

        LoginPage().show_window()


if __name__ == '__main__':
    UserModel().get_instance().create_user('adm23in', '2021-01-01', True, '123456789', 'adm23in', 0)
    AdminEmployees().show_window()
