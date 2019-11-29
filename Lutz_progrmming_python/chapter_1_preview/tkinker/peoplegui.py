import shelve
from tkinter import *
from tkinter.messagebox import showerror, showinfo

from Lutz_progrmming_python.chapter_1_preview.OOP.person import Person

shelve_name = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')
entries = {}


def make_widget():
    window = Tk()
    window.title('People Shelve')
    window.iconbitmap('favicon.ico')
    form = Frame(window)
    form.pack()
    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text='Fetch', command=fetch_record).pack(side=LEFT)
    Button(window, text='Update', command=update_record).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
    return window


def fetch_record():
    key = entries['key'].get()
    try:
        record = db[key]
    except KeyError:
        showerror(title='Error', message='No such key')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def update_record():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
        db[key] = record
    showinfo(title='Updating', message='The record has been update')


db = shelve.open(shelve_name)
win = make_widget()
win.mainloop()
db.close()
