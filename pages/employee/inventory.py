from tkinter import *


class InventoryPage:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.attributes('-zoomed', True)
        self.window.configure(bg="#35374f")
        self.user = None

        self.menu = Menu(self.window, bg="#535462", fg="white", activebackground="#9d9da4", activeforeground="white")
        self.menu.add_command(label='Return to Panel', command=self.go_to_panel)
        self.window.config(menu=self.menu)

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

    def show_page(self, user):
        self.user = user
        self.window.mainloop()

    def go_to_panel(self):
        from pages.employee.index import Main
        self.window.destroy()
        Main().show_window(user=self.user)
