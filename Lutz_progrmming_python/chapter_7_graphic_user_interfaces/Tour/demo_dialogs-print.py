from tkinter import *
from quitter import Quitter
from dialog_table import demos


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Basic demos').pack()
        for key in demos:
            func = lambda key=key: self.print_it(key)
            Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

    def print_it(self, name):
        print(name, '  returns => ', demos[name])


if __name__ == '__main__':
    Demo().mainloop()
