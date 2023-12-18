import tkinter as tk
from tkinter import ttk


class ScrollableFrame:
    def __init__(self, master):
        self.master = master
        self.master.title("Scrollable Frame Example")
        self.master.geometry("800x600")

        # Create a canvas and add a vertical scrollbar
        self.canvas = tk.Canvas(master)
        scrollbar = tk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Link the canvas to the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas
        self.inner_frame = ttk.Frame(self.canvas)

        # Add some widgets to the inner frame (replace this with your content)
        for i in range(20):
            ttk.Label(self.inner_frame, text=f"Label {i}").pack()

        # Create a window to hold the canvas
        self.canvas_frame = ttk.Frame(master)
        self.canvas_frame.pack(fill="both", expand=True)

        # Use the window to hold the canvas
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Bind the canvas to the mouse wheel to enable scrolling
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # Configure the canvas to expand and fill the window
        self.canvas_frame.bind("<Configure>", self.on_canvas_configure)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    root = tk.Tk()
    app = ScrollableFrame(root)
    root.mainloop()
