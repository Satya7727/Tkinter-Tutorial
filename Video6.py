from tkinter import Tk, Label, PhotoImage
from PIL import Image,ImageTk
# Pillow is install to be able to use jpg files in tkinter

root = Tk()
root.geometry("400x300")
# img = PhotoImage(file="download.png")

# For jpg images
img = Image.open("desk1.jpg")
photo = ImageTk.PhotoImage(img)
label = Label(root,image=photo)
label.pack()
root.mainloop()

# root = Tk()
# root.geometry("400x300")
# img = PhotoImage(file="download.png")
# label = Label(root, image=img)
# label.pack()
# root.mainloop()
