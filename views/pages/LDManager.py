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
        self.titles.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.device_list = tk.Frame(self)
        self.device_list.grid(row=3, column=0, sticky="w", padx=5)

        data = [
            (0, 'LDPlayer-0', '23'),
            (1, 'Jane Doe', '30'),
            (2, 'Bob Smith', '22'),
            (3, 'Alice Johnson', '28')
        ]

        self.id_devices = tk.Label(self.device_list, text="ID")
        self.id_devices.grid(row=0, column=0, sticky="w", padx=10)
        self.name_devices = tk.Label(self.device_list, text="Name")
        self.name_devices.grid(row=0, column=1, sticky="w", padx=10)
        self.name_devices = tk.Label(self.device_list, text="Name")
        self.name_devices.grid(row=0, column=1, sticky="w", padx=10)
