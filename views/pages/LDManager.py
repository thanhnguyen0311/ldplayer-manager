from threading import Thread
import queue
import time
import tkinter as tk

from ld_manager.create_ld import create_ld
from ld_manager.get_list_ld import get_list_ld
from ld_manager.quit_ld import quit_all
from ld_manager.remove_ld import remove_all_ld
from ld_manager.run_ld import run_ld


class LDManager_Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.task_queue = queue.Queue()
        self.data = get_list_ld()
        self.menu_bar = tk.Frame(self)
        self.menu_bar.grid(row=1, column=0, sticky="w", padx=5)

        self.button_add = tk.Button(self.menu_bar, text="Add", width=10, height=2, command=lambda: self.add_device(1))
        self.button_add.grid(row=0, column=0, padx=5, pady=5)
        self.button_get = tk.Button(self.menu_bar, text="Refresh", width=10, height=2, command=self.refresh)
        self.button_get.grid(row=0, column=1, padx=5, pady=5)
        self.button_get = tk.Button(self.menu_bar, text="Remove All", width=10, height=2, command=self.remove_all)
        self.button_get.grid(row=0, column=2, padx=5, pady=5)
        self.button_get = tk.Button(self.menu_bar, text="Kill All", width=10, height=2, command=self.kill_all)
        self.button_get.grid(row=0, column=3, padx=5, pady=5)
        self.button_get = tk.Button(self.menu_bar, text="Run All", width=10, height=2, command=self.run_all)
        self.button_get.grid(row=0, column=4, padx=5, pady=5)

        self.titles = tk.Label(self, text="Devices")
        self.titles.grid(row=2, column=0, padx=15, pady=5, sticky="w")

        self.device_list = tk.Frame(self)
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
        frame.uuid_devices = tk.Label(frame, text="Facebook")
        frame.uuid_devices.grid(row=0, column=4, sticky="w", padx=40, pady=5)
        frame.uuid_devices = tk.Label(frame, text="Status")
        frame.uuid_devices.grid(row=0, column=5, sticky="w", padx=50, pady=5)
        frame.uuid_devices = tk.Label(frame, text="Action")
        frame.uuid_devices.grid(row=0, column=6, sticky="w", padx=40, pady=5)

    def refresh(self):
        self.device_list.destroy()
        self.device_list = tk.Frame(self)
        self.device_frame()
        self.data = get_list_ld()
        for index, i in enumerate(self.data):
            self.device_line(i)

    def device_line(self, device):
        row = int(device.ID) + 1
        tk.Label(self.device_list, text=device.ID).grid(row=row, column=0)
        tk.Label(self.device_list, text=device.name).grid(row=row, column=1)
        tk.Label(self.device_list, text=device.imei).grid(row=row, column=2)
        tk.Label(self.device_list, text=device.uuid).grid(row=row, column=3)

    def add_device(self, number):
        thread = Thread(target=self.threaded_create, args=(number,))
        thread.start()

    def threaded_create(self, arg):
        for i in range(5):
            # create_ld(1)
            # self.refresh()
            print(i)
            time.sleep(1)

    def remove_all(self):
        remove_all_ld()
        self.refresh()

    def kill_all(self):
        quit_all()
        self.refresh()

    def run_all(self):
        thread = Thread(target=self.threaded_run)
        thread.start()

    def threaded_run(self):
        for index, device in enumerate(self.data):
            run_ld(device)
