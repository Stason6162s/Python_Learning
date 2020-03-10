from tkinter import *
from tkinter.colorchooser import askcolor


def set_bg_color():
    (RGB_str, HEX_str) = askcolor()
    if HEX_str:
        print(f'HEX: {HEX_str}')
        push.config(bg=HEX_str)


root = Tk()
push = Button(root, text='Set background color', command=set_bg_color)
push.config(height=3, font=('times', 20, 'bold'))
push.pack(expand=YES, fill=BOTH)
root.mainloop()
