from tkinter import *

X = 42


def handler(A, B):
    print(A * B)


def func():
    handler(X, 'Yam')


def hand_name(name):
    print(f"I'm {name}")

root = Tk()
Button(root, text='Lambda', command=lambda: handler(X, 'spam')).pack()
Button(root, text='Wrapper', command=func).pack()
Button(root, text='Bad_Name', command=hand_name('Bad name')).pack()
Button(root, text='Good_Name', command=lambda : hand_name('Good name')).pack()
mainloop()
