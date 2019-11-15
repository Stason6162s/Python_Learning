from tkinter import *

from Lutz_progrmming_python.chapter_1_preview.tkinker.tkinker102 import MyGui

main_win = Tk()
label = Label(main_win, text=__name__).pack()
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
main_win.mainloop()
