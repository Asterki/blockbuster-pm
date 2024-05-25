from tkinter import *
from tkinter import ttk, messagebox, simpledialog

from models.sales import SalesModel
from models.employees import EmployeeModel
from models.movies import MovieModel
from models.clients import ClientsModel
from services.logger import LoggerService


class AdminSales:
    def __init__(self):
        self.window = Tk()
        self.window.title('Movie Rental')
        self.window.geometry('800x500')
        self.window.attributes('-zoomed', True)
        self.window.config(bg="#35374f")
        self.user = None

        # Grid configuration
        for i in range(12):
            self.window.columnconfigure(i, weight=1)

        self.menu = Menu(self.window, bg="#535462", fg="white", activebackground="#9d9da4", activeforeground="white")
        self.menu.add_command(label="Logs", command=self.go_to_logs)
        self.menu.add_command(label='Employees', command=self.go_to_employees)
        self.menu.add_command(label="Rentals", command=self.go_to_rentals)
        self.menu.add_command(label='Clients', command=self.go_to_clients)
        self.menu.add_command(label='Movies', command=self.go_to_movies)
        self.menu.add_command(label='Admin Panel', command=self.go_to_admin)
        self.window.config(menu=self.menu)

        self.title = Label(self.window, text='Sales', font=('Fredoka', 25, "bold"), pady=20, fg="#d3aa1d", bg="#35374f")
        self.title.grid(row=0, column=1, columnspan=10, sticky="W")

        self.treeview = ttk.Treeview(self.window)
        self.treeview.grid(row=1, column=1, columnspan=10, rowspan=6, sticky="WE")

        self.treeview['columns'] = ('ID', 'Client', 'Movie', 'Employee', 'Date', 'Price sold')
        self.treeview.column('#0', width=0, stretch=NO)
        self.treeview.column('ID', anchor=W, width=50)
        self.treeview.column('Client', anchor=W, width=200)
        self.treeview.column('Movie', anchor=W, width=50)
        self.treeview.column('Employee', anchor=W, width=300)
        self.treeview.column('Date', anchor=W, width=150)
        self.treeview.column('Price sold', anchor=W, width=150)

        self.treeview.heading('#0', text='', anchor=W)
        self.treeview.heading('ID', text='ID', anchor=W)
        self.treeview.heading('Client', text='Client', anchor=W)
        self.treeview.heading('Movie', text='Movie', anchor=W)
        self.treeview.heading('Employee', text='Employee', anchor=W)
        self.treeview.heading('Date', text='Date', anchor=W)
        self.treeview.heading('Price sold', text='Price sold', anchor=W)

        # Movie action frame
        self.saleActionFrame = Frame(self.window, pady=10, padx=10, bg="#7c7d8b")
        self.saleActionFrame.grid(row=7, column=8, columnspan=3, sticky="WE")
        # Other actions
        Button(self.saleActionFrame, text="Find Sales by ID", command=self.find_sale_by_id, bg="#35374f", fg="white", activebackground="#3f425e", activeforeground="white").grid(row=7, column=12, sticky="E")
        Button(self.saleActionFrame, text="Reset Filter", command=self.get_sales, bg="#35374f", fg="white", activebackground="#3f425e", activeforeground="white").grid(row=7, column=13, sticky="E")
        self.get_sales()

    def get_sales(self):
        sales = SalesModel().get_instance().get_all_sales()
        for sale in sales:
            client = ClientsModel().get_instance().get_client(sale[1])
            movie = MovieModel().get_instance().get_movie(sale[2])
            employee = EmployeeModel().get_instance().get_employee(sale[3])

            self.treeview.insert('', 'end', text='', values=(sale[0], client[1], movie[1], employee[1], sale[4], sale[5]))

    def find_sale_by_id(self):
        try:
            sale_id = simpledialog.askinteger("Sale ID", "Enter the sale ID")
            sale = SalesModel().get_instance().get_sale(sale_id)
            if sale:
                client = ClientsModel().get_instance().get_client(sale[1])
                movie = MovieModel().get_instance().get_movie(sale[2])
                employee = EmployeeModel().get_instance().get_employee(sale[3])

                self.treeview.delete(*self.treeview.get_children())
                self.treeview.insert('', 'end', text='', values=(sale[0], client[1], movie[1], employee[1], sale[4], sale[5]))
            else:
                messagebox.showerror("Error", "Sale not found")
        except:
            messagebox.showerror("Error", "Invalid ID")

    # Navigation
    def show_window(self, user):
        self.user = user
        self.window.mainloop()

    def go_to_admin(self):
        from pages.admin.index import AdminMain
        self.window.destroy()
        AdminMain().show_window(user=self.user)

    def go_to_logs(self):
        from pages.admin.logs import AdminLogs

        self.window.destroy()
        AdminLogs().show_window(user=self.user)

    def go_to_movies(self):
        from pages.admin.movies import AdminMovies

        self.window.destroy()
        AdminMovies().show_window(user=self.user)

    def go_to_employees(self):
        from pages.admin.employees import AdminEmployees

        self.window.destroy()
        AdminEmployees().show_window(user=self.user)

    def go_to_rentals(self):
        from pages.admin.rentals import AdminRentals

        self.window.destroy()
        AdminRentals().show_window(user=self.user)

    def go_to_clients(self):
        from pages.admin.clients import AdminClients

        self.window.destroy()
        AdminClients().show_window(user=self.user)
