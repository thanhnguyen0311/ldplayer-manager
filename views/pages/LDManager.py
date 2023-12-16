import tkinter as tk
from tkinter import ttk


class LDManager_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.menu_bar = tk.Frame(self)
        self.menu_bar.grid(row=1, column=0, sticky="w")
        self.button_add = tk.Button(self.menu_bar, text="Add", width=10, height=2)
        self.button_add.grid(row=1, column=1, pady=5)
        self.button_get = tk.Button(self.menu_bar, text="Refresh", width=10, height=2)
        self.button_get.grid(row=1, column=2, pady=5)
        self.button_run = tk.Button(self.menu_bar, text="Run", width=10, height=2)
        self.button_run.grid(row=1, column=3, pady=5)
        self.button_delete = tk.Button(self.menu_bar, text="Delete", width=10, height=2)
        self.button_delete.grid(row=1, column=4, pady=5)
        self.titles = tk.Label(self, text="Devices")

        self.titles.grid(row=2, column=0,pady=5, sticky="w")
        self.tree = ttk.Treeview(self, columns=('ID', 'Name', 'Age'))

        # Define column headings
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='Age')

        # Add sample data to the table
        data = [
            ('1', 'John Doe', '25'),
            ('2', 'Jane Doe', '30'),
            ('3', 'Bob Smith', '22'),
            ('4', 'Alice Johnson', '28')
        ]

        for row in data:
            self.tree.insert('', 'end', values=row)

        # Pack the Treeview widget
        self.tree.grid(row=3, column=0, sticky="w")
