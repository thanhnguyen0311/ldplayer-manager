import tkinter as tk


class Setting(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        tk.Label(self, text="This is Setting Page").pack(side=tk.LEFT)
