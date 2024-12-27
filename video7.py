# Attributes of label and pack
from tkinter import  *
root = Tk()
root.title("Attributes of label")
root.geometry("700x400")

# Important label options

# text-Adds the text
# bd,bg-Background
# fg-forground
# font - sets the font
# 1.font=("comicsansms",19,"bold")
# 2,font = "comicsansms 19 bold"
# padx-padding  in x dirextion
# pady-padding in y direction
# relief-border styling-SUNKEN,GROOVE,RIDGE,RAISED

title_label = Label(root,text='''In a career spanning over three decades
                              \nKhan has received numerous awards, incl
                              \n Film Awards as a film producer, and tw
                              \nHe is cited in the media as one of theh
                              \n successful actors of Indian cinema.''', fg="white",bg="red",padx=23,pady=23,font=("comicsansms",9,"bold"),borderwidth=3,relief=RIDGE)

#Important pack options
# anchor = nw or ne ->to set the positions of label 
# side = LEFT,BOTTOM,TOP,RIGHT 
# fill->
# padx->
# pady->
# title_label.pack(side=BOTTOM,anchor="w",fill=X)
title_label.pack(side=LEFT,fill=Y,padx=10,pady=10)

root.mainloop()