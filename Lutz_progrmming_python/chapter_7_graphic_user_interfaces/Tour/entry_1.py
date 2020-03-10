from tkinter import *
from quitter import Quitter

def fetch():
	print(f"Input => {entry.get()}")


root =Tk()
entry = Entry(root)
entry.insert(0, 'Type')
entry.config(show='☺')
entry.pack(side=TOP, fill=X)
entry.focus()
entry.bind('<Return>', lambda event: fetch())
fetch_btn =Button(root, text='Fetch', command=fetch)
fetch_btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()