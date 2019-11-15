from tkinter import *
from tkinter.messagebox import showinfo


def reply():
    showinfo('Popup', message='Button pressed')


window = Tk()
button = Button(window, text='Push', command=reply)
button.pack()
window.mainloop()
