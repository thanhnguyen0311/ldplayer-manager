import tkinter as tk
from views.pages.LDManager import LDManager_Page


class MainFrame(tk.Frame):
    def __init__(self):
        super().__init__(highlightbackground='black', highlightthickness=1, bg='#F0FFFF')
        self.frame = None
        self.pack(side=tk.LEFT, fill=tk.Y)
        self.pack_propagate(False)
        self.configure(width=650)
        self.choose_page(LDManager_Page)

    # def show_frame(self, container):
    #     container.tkraise()

    def delete_pages(self):
        for frame in self.winfo_children():
            frame.destroy()

    def choose_page(self, page):
        self.delete_pages()
        self.frame = page(self)
        self.frame.pack()
