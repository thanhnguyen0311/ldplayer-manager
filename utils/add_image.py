import tkinter as tk
from PIL import ImageTk, Image


def RBGAImage(path):
    return Image.open(path).convert("RGBA")


def show_image(frame, path, width, height):
    im = RBGAImage(path)
    print(im.mode)
    canvas = tk.Canvas(frame, bg="lightblue", width=width, height=height)
    frame.photo_image = ImageTk.PhotoImage(im.resize((75, 75)))
    canvas.create_image(width/2, height/2, image=frame.photo_image)
    # frame.img = ImageTk.PhotoImage(im.resize((width, height)))
    # frame.image_label = tk.Label(frame, image=frame.img)

    return canvas
