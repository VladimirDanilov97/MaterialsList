from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()
root.title('Icons')
root.geometry('400x400')
cwd = os.getcwd()
root.iconbitmap(os.path.join(cwd, 'icons', '1.ico'))

options = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday'
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

lbl = Label(root, text='')
lbl.pack()

def show():
    lbl.config(text=clicked.get())

btn = Button(root, text='Select', command=show)
btn.pack()

root.mainloop()