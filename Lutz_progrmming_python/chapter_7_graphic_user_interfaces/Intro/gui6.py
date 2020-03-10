from tkinter import *


class MyFrame(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 0
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self, text='Frame button', command=self.messages)
        widget.pack(side=LEFT)

    def messages(self):
        self.data += 1
        print(f'{self.data=}')

if __name__ == '__main__':
    MyFrame().mainloop()