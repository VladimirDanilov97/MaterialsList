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

status = Label(
    root,
    text=f'Image {i+1} of {len(img_lst)}',
    bd=1,
    relief=SUNKEN,
    anchor=E)

def update_status(i):
    status.config(text=f'Image {i+1} of {len(img_lst)}')


def back():
    global i
    global my_label
    global img_lst

    if i > 0: 
        i -= 1
    else: 
        i = len(img_lst)-1
    update_status(i)
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
        
    update_status(i)
    my_label.grid_forget()
    my_label = Label(image=img_lst[i])
    my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text='<<', command=back)
button_forward = Button(root, text='>>', command=forward)
button_quit = Button(root, text='Exit', command=root.quit)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=W+E)


root.mainloop()
