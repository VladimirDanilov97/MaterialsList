from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()
root.title('Icons')

cwd = os.getcwd()
root.iconbitmap(os.path.join(cwd, 'icons/1.ico'))



my_image = ImageTk.PhotoImage(Image.open('./icons/2.png'))
my_label = Label(image=my_image).pack()

button_quit = Button(root, text='Exit', command=root.quit).pack()

root.mainloop()
