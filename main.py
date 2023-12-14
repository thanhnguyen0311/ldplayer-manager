import tkinter as tk
from views.layouts.SideBar import SideBar


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        home_page = HomePage()


class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title("Social Marketing Tool")
        self.geometry("800x600")
        side_bar = SideBar()


if __name__ == '__main__':
    app = Login()
    app.mainloop()
