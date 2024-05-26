from tkinter import *


class RentalsPage:
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

        # For this page, buttons are: New Sale, Check Sale, Check Inventory, Logout, Register Member, Add Review
        # Remove review, make rental, return rental

        # New Sale
        new_sale = Button(self.window, text='New Sale', command=self.new_sale)
        new_sale.grid(row=1, column=1, sticky='nsew')

        # Check Sale
        check_sale = Button(self.window, text='Check Sale', command=self.check_sale)
        check_sale.grid(row=1, column=2, sticky='nsew')

        # Check Inventory
        check_inventory = Button(self.window, text='Check Inventory', command=self.check_inventory)
        check_inventory.grid(row=1, column=3, sticky='nsew')

        # Logout
        logout = Button(self.window, text='Logout', command=self.logout)
        logout.grid(row=1, column=4, sticky='nsew')

        # Register Member
        register_member = Button(self.window, text='Register Member', command=self.register_member)
        register_member.grid(row=1, column=5, sticky='nsew')

        # Add Review
        add_review = Button(self.window, text='Add Review', command=self.add_review)
        add_review.grid(row=1, column=6, sticky='nsew')

        # Remove Review
        remove_review = Button(self.window, text='Remove Review', command=self.remove_review)
        remove_review.grid(row=1, column=7, sticky='nsew')

        # Make Rental
        make_rental = Button(self.window, text='Make Rental', command=self.make_rental)
        make_rental.grid(row=1, column=8, sticky='nsew')

        # Return Rental
        return_rental = Button(self.window, text='Return Rental', command=self.return_rental)
        return_rental.grid(row=1, column=9, sticky='nsew')

        self.window.mainloop()

    def show_page(self, user):
        self.user = user
        self.window.mainloop()

    def go_to_panel(self):
        from pages.employee.index import Main
        self.window.destroy()
        Main().show_window(user=self.user)

    def new_sale(self):
        pass

    def check_sale(self):
        pass
