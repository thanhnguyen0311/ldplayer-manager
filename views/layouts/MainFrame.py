import tkinter as tk

from views.pages.LDManager import LDManager_Page


class MainFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.Frame = None
        self.choose_page(LDManager_Page)

    def delete_pages(self):
        for frame in self.winfo_children():
            frame.destroy()

    def choose_page(self, page):
        self.delete_pages()
        self.Frame = page(self)
        self.Frame.pack(side=tk.LEFT, fill=tk.BOTH)
