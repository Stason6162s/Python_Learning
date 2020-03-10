import sys
from tkinter import Toplevel, Button, Label

win_1 = Toplevel()
win_2 = Toplevel()

Button(win_1, text='spam', command=sys.exit).pack()
Button(win_2, text='SPAM', command=sys.exit).pack()

Label(text='Popups').pack()
win_1.mainloop()
