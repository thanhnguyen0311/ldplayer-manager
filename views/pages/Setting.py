import tkinter as tk
from tkinter import ttk


class Setting(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is Setting Page").pack(side=tk.LEFT)
