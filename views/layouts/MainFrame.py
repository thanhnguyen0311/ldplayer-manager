import tkinter as tk

from views.pages.LDManager import LDManager_Page


class MainFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.Frame = None
        self.configure(width=650)
        self.choose_page(LDManager_Page)

    def delete_pages(self):
        for frame in self.winfo_children():
            frame.destroy()

    def choose_page(self, page):
        self.delete_pages()
        self.Frame = page(self)
        self.Frame.pack()
