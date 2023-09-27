import pyqrcode
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# To generate NAME and LINK make a function
def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 280, window=image_label)

canvas = Canvas(root, width=400, height=300)
canvas.pack()

app_label = Label(root, text="QR code Generator", fg="blue", font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text='link name')
canvas.create_window(200, 100, window=name_label)
link_label = Label(root, text="link")
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
canvas.create_window(200, 120, window=name_entry)
link_entry = Entry(root)
canvas.create_window(200, 180, window=link_entry)

button = Button(root, text="Generate QR code", command=generate)
canvas.create_window(200, 220, window=button)
root.mainloop()