from tkinter import *


class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('500x500')
        self.window.resizable(False, False)

        self.label = Label(self.window, text='Welcome to Movie Rental', font=('Arial', 20))
        self.label.pack()

        self.button = Button(self.window, text='Login', font=('Arial', 15))
        self.button.pack()

        self.window.mainloop()

    def show_window(self):
        self.window.mainloop()


if __name__ == '__main__':
    Main()
