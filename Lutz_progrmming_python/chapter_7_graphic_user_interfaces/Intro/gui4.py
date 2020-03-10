from tkinter import *


def greeting():
    print('Hello stdout world!...')


window = Frame()
window.pack(side=TOP, expand=YES, fill=BOTH)
Label(window, text='Text container').pack(side=TOP, expand=YES)
Button(window, text='Hello', command=greeting).pack(side=LEFT)
Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
window.mainloop()
