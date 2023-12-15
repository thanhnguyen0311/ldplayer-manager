import tkinter as tk
from views.pages.LDManager import LDManager_Page


class MainFrame(tk.Frame):
    def __init__(self):
        super().__init__(highlightbackground='black', highlightthickness=2, bg='white')
        self.pack(side=tk.LEFT, fill=tk.Y)
        self.pack_propagate(False)
        self.configure(width=650)
        self.choose_page(LDManager_Page)

    def delete_pages(self):
        for frame in self.winfo_children():
            frame.destroy()

    def choose_page(self, page):
        self.delete_pages()
        page(self)
