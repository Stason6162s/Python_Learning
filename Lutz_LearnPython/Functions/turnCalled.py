import sys
from tkinter import Button, mainloop

x = Button(
    text='Press me',
    command=lambda: sys.stdout.write("Spam\n")
)
x.pack()
mainloop()
print("Hi, men! We are on new home. Viva new life!!")