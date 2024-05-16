from tkinter import *
from tkinter import ttk

from services.logger import LoggerService


class AdminLogs:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.resizable(False, False)

        self.treeview = ttk.Treeview(self.window)
        self.treeview.pack()

        self.treeview['columns'] = ('Username', 'Action', 'Date')
        self.treeview.column('#0', width=0, stretch=NO)
        self.treeview.column('Username', anchor=W, width=100)
        self.treeview.column('Action', anchor=W, width=100)
        self.treeview.column('Date', anchor=W, width=100)

        self.treeview.heading('#0', text='', anchor=W)
        self.treeview.heading('Username', text='Username', anchor=W)
        self.treeview.heading('Action', text='Action', anchor=W)
        self.treeview.heading('Date', text='Date', anchor=W)

        self.button = Button(self.window, text='Go Back', font=('Arial', 15), command=self.go_back)
        self.button.pack()

        self.get_and_show_logs()
        self.window.mainloop()

    def get_and_show_logs(self):
        logs = LoggerService().get_instance().get_logs()
        for log in list(logs):
            self.treeview.insert(parent='', index=0, iid=0, text='', values=(log[1], log[2], log[3]))

    def show_window(self):
        self.window.mainloop()

    def go_back(self):
        from pages.admin.index import AdminMain
        self.window.destroy()
        AdminMain().show_window()
