from tkinter import *
from tkinter.messagebox import *


def callback():
    if askyesno('Ask Yes / No', 'Do you really want to quit?'):
        showwarning('Warning', 'Quit not yet implemented')
    else:
        showinfo('Info', 'Quit has been cancelled')


err_msg = 'Sorry, no Spam allowed'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Error', err_msg))).pack(fill=X)

mainloop()
