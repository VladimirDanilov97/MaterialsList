from tkinter import *
import os
from PIL import Image, ImageTk

root = Tk()
root.title('Icons')
root.iconbitmap(os.path.join(os.getcwd(), 'icons', '1.ico'))
my_img = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), 'images', '1.png')))

def open_window():
    top = Toplevel()
    top.title('Image')
    lbl = Label(top, image=my_img).pack()
    btn2= Button(top, text='Close', command=top.destroy).pack()


btn= Button(root, text='open window', command=open_window)
btn.pack()

root.mainloop()