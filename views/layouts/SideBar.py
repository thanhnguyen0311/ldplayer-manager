import tkinter as tk
from views.layouts.MainFrame import MainFrame
from views.pages.LDManager import LDManager_Page


class SideBar(tk.Frame):
    def __init__(self, bg='lightblue'):
        super().__init__(bg=bg)
        self.pack(side=tk.LEFT, fill=tk.Y)
        self.pack_propagate(False)
        self.configure(width=150)
        main_frame = MainFrame()
        tk.Label(self, text="Social Marketing Tool").pack(pady=50)
        button_LDManager = tk.Button(self, text="LDManager", width=150, height=2,
                                     command=lambda: main_frame.choose_page(LDManager_Page))
        button_LDManager.pack()
        tk.Button(self, text="Setting", width=150, height=2).pack()
        tk.Button(self, text="Exit", width=150, height=2).pack()
