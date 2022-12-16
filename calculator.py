from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def plus():
    first_number = e.get()
    if first_number:
        global f_num
        global math 
        math = 'addition'
        f_num = int(first_number)
        e.delete(0, END)

def subtract():
    first_number = e.get()
    if first_number:
        global f_num
        global math 
        math = 'subtract'
        f_num = int(first_number)
        e.delete(0, END)

def multiply():
    first_number = e.get()
    if first_number:
        global f_num
        global math 
        math = 'multiply'
        f_num = int(first_number)
        e.delete(0, END)

def division():
    first_number = e.get()
    if first_number:
        global f_num
        global math 
        math = 'division'
        f_num = int(first_number)
        e.delete(0, END)


def equal():
    second_number = e.get()
    e.delete(0, END)
    if f_num and second_number:
        if math=='addition':
            e.insert(0, f_num+int(second_number))
        if math=='subtraction':
            e.insert(0, f_num-int(second_number))
        if math=='multiply':
            e.insert(0, f_num*int(second_number))
        if math=='division':
            if int(second_number) !=0:
                e.insert(0, f_num/int(second_number))

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_plus = Button(root, text='+', padx=39, pady=20, command=plus)
button_subtract = Button(root, text='-', padx=40, pady=20, command=subtract)
button_multiply = Button(root, text='*', padx=40, pady=20, command=multiply)
button_division = Button(root, text='/', padx=40, pady=20, command=division)


button_equal = Button(root, text='=', padx=91, pady=20, command=equal)
button_clear = Button(root, text='Clear', padx=79, pady=20, command=clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_division.grid(row=6, column=2)

root.mainloop()
