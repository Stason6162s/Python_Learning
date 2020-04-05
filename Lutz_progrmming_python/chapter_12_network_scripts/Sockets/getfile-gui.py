import os, sys
from tkinter import *
from tkinter.messagebox import showinfo


def on_return_key():
    cmd_line = f"python getfile.py - mode client -file {content['File'].get()} -port {content['Port'].get()}" \
               f" -host {content['Host'].get()}"
    os.system(cmd_line)
    showinfo('getfilegui-1', 'Download completed')


box = Tk()
labels = ['File', 'Port', 'Host']
content = {}
for label in labels:
    row = Frame(box)
    row.pack(fill=X)
    Label(row, text=label, width=6).pack(side=LEFT)
    entry = Entry(row)
    entry.pack(side=RIGHT, expand=YES, fill=X)
    content[label] = entry
box.title('getfilegui-1')
box.bind('<Return>',lambda event: on_return_key())
mainloop()