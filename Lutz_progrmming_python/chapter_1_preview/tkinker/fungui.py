import random
from tkinter import *

font_size = 30
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'purple']


def on_spam():
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Popup', bg='black', fg=color).pack(fill=BOTH)
    main_label.config(fg=color)


def on_flip():
    main_label.config(fg=random.choice(colors))
    main.after(250, on_flip)


def on_grow():
    global font_size
    font_size += 5
    main_label.config(font=('arial', font_size, 'italic'))
    main.after(100, on_grow)


main = Tk()
main_label = Label(main, text='Fun Gui!', relief=RAISED)
main_label.config(font=('arial', font_size, 'italic'), fg='cyan', bg='navy')
main_label.pack(side=TOP, expand=YES, fill=BOTH)
Button(main, text='Spam', command=on_spam).pack(fill=X)
Button(main, text='Flip', command=on_flip).pack(fill=X)
Button(main, text='Grow', command=on_grow).pack(fill=X)
main.mainloop()
