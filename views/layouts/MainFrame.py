import tkinter as tk

from views.pages.LDManager import LDManager_Page


class MainFrame(tk.Frame):
    def __init__(self, page):
        tk.Frame.__init__(self)
        self.canvas_scrollbar_pairs = []
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.Frame = page(self)
        self.canvas.create_window((0, 0), window=self.Frame, anchor="nw")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        if page == LDManager_Page:
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.bind("<Configure>", self.on_configure)

    def on_configure(self, event):
        # Update the scroll region to encompass the entire canvas
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


