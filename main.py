import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import ttkbootstrap as tb


def disable_resize(event=None):
    return False


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title("Social Marketing Tool")
        self.geometry("800x600")

        menu_frame = tk.Frame(self, bg='lightblue')
        menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        menu_frame.pack_propagate(False)
        menu_frame.configure(width=150)

        tk.Label(menu_frame, text="Social Marketing Tool").pack(pady=50)
        tk.Button(menu_frame, text="LDManager", width=150, height=2).pack()
        tk.Button(menu_frame, text="Setting", width=150, height=2).pack()
        tk.Button(menu_frame, text="Exit", width=150, height=2).pack()

        main_frame = tk.Frame(self, highlightbackground='black', highlightthickness=2, bg='white')
        main_frame.pack(side=tk.LEFT, fill=tk.Y)
        main_frame.pack_propagate(False)
        main_frame.configure(width=650)


if __name__ == '__main__':
    app = App()
    app.mainloop()
