import tkinter as tk

from views.pages.LDManager import LDManager_Page


class MainFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.scrollbar = tk.Scrollbar(self)
        self.canvas_scrollbar_pairs = []
        self.canvas = tk.Canvas(self)
        self.Frame = None
        self.choose_page(LDManager_Page)

    def delete_pages(self):
        children = list(self.children.values())
        for child in children:
            child.destroy()

        for frame in self.winfo_children():
            frame.destroy()

    def choose_page(self, page):
        self.delete_pages()
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.Frame = page(self.canvas)
        self.canvas.create_window((0, 0), window=self.Frame, anchor="nw")
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.on_configure)
        self.canvas_scrollbar_pairs.append([self.canvas, self.scrollbar])

    def on_configure(self, event):
        # Update the scroll region to encompass the entire canvas
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
