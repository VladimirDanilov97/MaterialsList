from tkinter import *
import os

root = Tk()
root.title('Icons')
root.iconbitmap(os.path.join(os.getcwd(), 'icons', '1.ico'))

MODES = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion')
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in MODES:

    Radiobutton(root, text=text, value=mode, variable=pizza).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

def clicked(value):
    myLabel.config(text=value)

button = Button(root, text='Add', command=lambda: clicked(pizza.get()))
button.pack()
root.mainloop()