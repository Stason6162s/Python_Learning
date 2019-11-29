from tkinter import *
from tkinter.messagebox import showinfo


def reply(name):
    showinfo('Reply', 'Hello %s!' % name)


win = Tk()
win.title('Echo')
win.iconbitmap('favicon.ico')

Label(win, text='Enter your name:').pack(side=TOP)
enter_box = Entry(win)
enter_box.pack(side=TOP)
button = Button(win, text='Submit', command=(lambda: reply(enter_box.get())))
button.pack(side=RIGHT)

win.mainloop()

