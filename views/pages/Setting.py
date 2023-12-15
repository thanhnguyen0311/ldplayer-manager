import tkinter as tk
from tkinter import ttk


class Setting(ttk.Frame):
    def __init__(self, main_frame):
        super().__init__()
        tk.Label(main_frame, text="This is Setting Page").pack(side=tk.LEFT)
