# Frames in tkinter
from tkinter import *
root=Tk()
root.title("Frames")
root.geometry("655x233")
f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
f2=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
l1=Label(f1,text="THIS IS A BASIC FRAME")
l1.pack(pady=10,padx=20)
l2=Label(f2,text="THIS IS A BASIC FRAME")
l2.pack(pady=10)

root.mainloop()