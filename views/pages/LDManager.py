import time
import tkinter as tk

from ld_manager.create_ld import create_ld
from ld_manager.get_list_ld import get_list_ld


class LDManager_Page(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.data = get_list_ld()
        self.menu_bar = tk.Frame(self)
        self.menu_bar.grid(row=1, column=0, sticky="w", padx=5)

        self.button_add = tk.Button(self.menu_bar, text="Add", width=10, height=2, command=self.add_device)
        self.button_add.grid(row=1, column=1, pady=5)
        self.button_get = tk.Button(self.menu_bar, text="Refresh", width=10, height=2, command=self.refresh)
        self.button_get.grid(row=1, column=2, pady=5)

        self.titles = tk.Label(self, text="Devices")
        self.titles.grid(row=2, column=0, padx=15, pady=5, sticky="w")

        self.device_list = tk.Frame(self)
        self.device_frame()
        self.refresh()

    def device_frame(self):
        frame = self.device_list
        self.device_list.grid(row=3, column=0, sticky="w", padx=0)

        frame.id_devices = tk.Label(frame, text="ID")
        frame.id_devices.grid(row=0, column=0, sticky="w", padx=20, pady=5)
        frame.name_devices = tk.Label(frame, text="Name")
        frame.name_devices.grid(row=0, column=1, sticky="w", padx=30, pady=5)
        frame.imei_devices = tk.Label(frame, text="IMEI")
        frame.imei_devices.grid(row=0, column=2, sticky="w", padx=40, pady=5)
        frame.uuid_devices = tk.Label(frame, text="UUID")
        frame.uuid_devices.grid(row=0, column=3, sticky="w", padx=40, pady=5)

    def refresh(self):
        self.device_list.destroy()
        self.device_list = tk.Frame(self)
        self.device_frame()
        self.data = get_list_ld()
        for index, i in enumerate(self.data):
            self.device_line(index + 1, i)

    def device_line(self, index, device):
        tk.Label(self.device_list, text=device.ID).grid(row=device.ID, column=0)
        tk.Label(self.device_list, text=device.name).grid(row=device.ID, column=1)
        tk.Label(self.device_list, text=device.imei).grid(row=device.ID, column=2)
        tk.Label(self.device_list, text=device.uuid).grid(row=device.ID, column=3)

    def add_device(self):
        device = create_ld(1)
        self.refresh()

