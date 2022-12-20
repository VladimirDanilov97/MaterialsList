from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()
root.title('Icons')
root.geometry('400x400')
cwd = os.getcwd()
root.iconbitmap(os.path.join(cwd, 'icons', '1.ico'))

var = StringVar()

c = Checkbutton(root, text='Check this!',
                variable=var, onvalue='On',
                offvalue='Off')
c.deselect()
c.select()
c.pack()


lbl = Label(root, text='')
lbl.pack()

def update():
    lbl.config(text=var.get())

btn = Button(root, text='Click', command=update)
btn.pack()




root.mainloop()