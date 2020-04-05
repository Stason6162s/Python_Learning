from tkinter import *

entry_size = 40


class Form:
    def __init__(self, labels, parent=None):
        label_size = max(len(item) for item in labels) + 2
        window = Frame(parent)
        window.pack(expand=YES, fill=X)
        rows = Frame(window, bd=2, relief=GROOVE)
        rows.pack(side=TOP, expand=YES, fill=X)
        self.content = {}
        for label in labels:
            row = Frame(rows)
            row.pack(fill=X)
            Label(row, text=label, width=label_size).pack(side=LEFT)
            entry = Entry(row, width=entry_size)
            entry.pack(side=RIGHT, expand=YES, fill=X)
            self.content[label] = entry
        Button(window, text='Cancel', command=self.on_Cancel).pack(side=RIGHT)
        Button(window, text='Submit', command=self.on_Submit).pack(side=RIGHT)

    def on_Cancel(self):
        Tk().quit()

    def on_Submit(self):
        for key in self.content:
            print(key, '\t=>\t', self.content[key].get())


class DynamicForm(Form):
    def __init__(self, labels=None):
        labels = input('Enter field names: ').split()
        Form.__init__(self, labels)

    def on_Submit(self):
        print('Field values...')
        Form.on_Submit(self)
        self.on_Cancel()


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        Form(['Name', 'Age', 'Job'])
    else:
        DynamicForm()
    mainloop()
