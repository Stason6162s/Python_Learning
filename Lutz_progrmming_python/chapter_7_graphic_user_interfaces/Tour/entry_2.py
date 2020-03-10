from tkinter import *
from quitter import Quitter

FIELDS = 'Name', 'Job', 'Pay'

def fetch(entries):
	for entry in entries:
		print(f'Input => {entry.get()}')


def make_form(root,  fields):
	entries =[]
	for field in fields:
		row = Frame(root)
		label = Label(row, width=5, text=field)
		entry = Entry(row)
		row.pack(side=TOP, fill =X)
		label.pack(side=LEFT)
		entry.pack(side=RIGHT, fill=X, expand=YES)
		entries.append(entry)
	return entries


if __name__ == '__main__':
	root =Tk()
	ents = make_form(root, FIELDS)
	root.bind('<Return>', lambda event:fetch(ents))
	Button(root, text='Fetch', command = lambda : fetch(ents)).pack(side=LEFT)
	Quitter(root).pack(side=RIGHT)
	root.mainloop()