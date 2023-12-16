import tkinter as tk
from tkinter import ttk


class LDManager_Page(tk.Frame):
    def __init__(self, main_frame):
        super().__init__()
        tk.Label(main_frame, text="This is LDManager Page").pack(side=tk.LEFT)
