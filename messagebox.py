from tkinter import *
import os
from tkinter import messagebox
root = Tk()
root.title('Icons')
root.iconbitmap(os.path.join(os.getcwd(), 'icons', '1.ico'))

#showinfo, showwarning, askquestion, showerror, askokcancel, askyesno

def popup():
    responce = messagebox.showwarning('This is Popup!', 'Hello, World!')
    Label(root, text=responce).pack()

Button(root, text='Popup', command=popup).pack()

root.mainloop()