from tkinter import *

from quitter import Quitter

FIELDS = 'Name', 'Job', 'Pay'


def fetch(variables):
    for variable in variables:
        print(f'Input => {variable.get()}')


def make_form(root, fields):
    form = Frame(root)
    left = Frame(form)
    right = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    right.pack(side=RIGHT, fill=X, expand=YES)

    variables = []
    for field in fields:
        label = Label(left, text=field, width=5)
        entry = Entry(right)
        label.pack(side=TOP)
        entry.pack(side=TOP, fill=X)
        var = StringVar()
        entry.config(textvariable=var)
        var.set("Type here")
        variables.append(var)
    return variables


if __name__ == '__main__':
    root = Tk()
    vars = make_form(root, FIELDS)
    Button(root, text='Fetch', command=lambda: fetch(vars)).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', lambda event: fetch(vars))
    root.mainloop()
