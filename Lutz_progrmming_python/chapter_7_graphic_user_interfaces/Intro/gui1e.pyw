from tkinter import *
import time


def quit():
    print('Hello, i must be going....')
    message_label.config(text='Hello, i must be going....')
    sys.exit()


Label(text='Extended GUI world! ').pack(expand=YES, fill=BOTH)
message_label = Label(text='Messages')
message_label.pack(expand=YES, fill=BOTH)
Button(None, text='SYS.EXIT', command=sys.exit).pack(side=LEFT, expand=YES, fill=BOTH)  # Прерывает приложение
Button(None, text='ROOT.QUIT', command=sys.exit).pack(side=RIGHT, expand=YES, fill=BOTH)  # Закрытвает все окна
Button(None, text='FUNC.EXIT', command=quit).pack(side=RIGHT, expand=YES, fill=BOTH)  # Регистрируем свой обработчик
Button(None, text='LAMBDA.EXIT', command=lambda: print('Hello lambda world!' or sys.exit())).pack(side=RIGHT, expand=YES,
                                                                                                fill=BOTH)
mainloop()
