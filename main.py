import tkinter as tk
from views.layouts.SideBar import SideBar


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        HomePage()


class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LDManager Tool")
        self.geometry("1200x600")
        SideBar(self)


if __name__ == '__main__':
    app = HomePage()
    app.mainloop()
