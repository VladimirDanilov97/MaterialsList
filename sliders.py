from tkinter import *
import os
from PIL import Image, ImageTk

def slide(horizontal):
    my_label.config(text=horizontal)

root = Tk()
root.title('Icons')
root.iconbitmap(os.path.join(os.getcwd(), 'icons', '1.ico'))
root.geometry('400x400')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=slide)
horizontal.pack()

my_label = Label(root, text=horizontal.get())
my_label.pack()



btn = Button(root, text='Click', command=slide)
btn.pack()

root.mainloop()
