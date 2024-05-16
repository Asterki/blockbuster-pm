from tkinter import *

from pages.login import LoginPage
from pages.admin.logs import AdminLogs
from models.users import UserModel


class Main:
    def __init__(self):
        # UserModel().get_instance().create_user('admin', '2021-01-01', True, '123456789', 'admin', 0)
        LoginPage().show_window()


if __name__ == '__main__':
    Main()
