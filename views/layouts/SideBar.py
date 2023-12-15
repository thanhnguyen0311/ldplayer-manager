import tkinter as tk

from views.layouts.MainFrame import MainFrame
from views.pages.LDManager import LDManager_Page
from views.pages.Setting import Setting
from constants.constants import LOGO_PATH
from utils.add_image import show_image


def close_app(app):
    app.destroy()


class SideBar(tk.Frame):
    def __init__(self, home_page, bg='lightblue'):
        super().__init__(bg=bg)
        self.pack(side=tk.LEFT, fill=tk.Y)
        self.pack_propagate(False)
        self.configure(width=150)
        main_frame = MainFrame()

        img = show_image(self, LOGO_PATH, 150, 150)
        img.pack(padx=10,pady=50)

        self.button_LDManager = tk.Button(self, text="LDManager", width=150, height=2,
                                          command=lambda: main_frame.choose_page(LDManager_Page))
        self.button_LDManager.pack()

        self.button_setting = tk.Button(self, text="Setting", width=150, height=2,
                                        command=lambda: main_frame.choose_page(Setting))
        self.button_setting.pack()

        self.button_exit = tk.Button(self, text="Exit", width=150, height=2,
                                     command=lambda: close_app(home_page))
        self.button_exit.pack()
