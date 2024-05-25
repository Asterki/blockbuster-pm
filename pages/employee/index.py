from tkinter import *


class Main:
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

        self.label = Label(self.window, text='Welcome to Blockbuser PM', font=('Arial', 20))
        self.label.pack()

        self.button = Button(self.window, text='Login', font=('Arial', 15))
        self.button.pack()

        self.window.mainloop()

    def show_window(self, user):
        self.user = user
        self.window.mainloop()
