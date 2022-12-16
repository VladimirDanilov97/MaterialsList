from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()
root.title('Icons')

cwd = os.getcwd()
root.iconbitmap(os.path.join(cwd, 'icons', '1.ico'))

img_path = os.path.join(cwd, 'images')
img_lst = os.listdir(img_path)
img_lst = list(map(lambda img: ImageTk.PhotoImage(Image.open(os.path.join(img_path, img))), img_lst))

i = 0
my_label = Label(image=img_lst[i])
my_label.grid(row=0, column=0, columnspan=3)

def back():
    global i
    global my_label
    global img_lst

    if i > 0: 
        i -= 1
    else: 
        i = len(img_lst)-1

    my_label.grid_forget()
    my_label = Label(image=img_lst[i])
    my_label.grid(row=0, column=0, columnspan=3)


def forward():
    global i
    global my_label
    global img_lst

    if i < len(img_lst)-1: 
        i += 1
    else:
        i = 0

    my_label.grid_forget()
    my_label = Label(image=img_lst[i])
    my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text='<<', command=back)
button_forward = Button(root, text='>>', command=forward)
button_quit = Button(root, text='Exit', command=root.quit)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)



root.mainloop()
