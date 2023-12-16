import tkinter as tk
from tkinter import ttk


class LDManager_Page(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, highlightbackground='black', highlightthickness=2, bg='#EDF2FB')
        self.pack(side=tk.LEFT, fill=tk.Y)
        self.button_add = tk.Button(self, text="Add", width=10, height=2)
        self.button_add.grid(row=1, column=1, padx=5, pady=5)
        self.button_get = tk.Button(self, text="Get List LD", width=10, height=2)
        self.button_get.grid(row=1, column=2, padx=5, pady=5)
        self.button_run = tk.Button(self, text="Run", width=10, height=2)
        self.button_run.grid(row=1, column=3, padx=5, pady=5)
        self.button_delete = tk.Button(self, text="Delete", width=10, height=2)
        self.button_delete.grid(row=1, column=4, padx=5, pady=5)
