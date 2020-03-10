from tkinter import *


def show_position_event(event):
    print(f"Widget = {event.widget} X = {event.x} Y = {event.y}")


def show_all_events(event):
    print(event)
    for attr in dir(event):
        if not attr.startswith('__'):
            print(f'{attr} => {getattr(event, attr)}')


def on_key_press(event):
    print(f'Got key press {event.char}')


def on_arrow_key(event):
    print('Got up arrow key press')


def on_return_key(event):
    print('Got return key press')


def on_left_click(event):
    print('Got left mouse button click: ', end=' ')
    show_position_event(event)


def on_right_click(event):
    print('Got right mouse button click: ', end=' ')
    show_position_event(event)


def on_middle_click(event):
    print('Got middle mouse button click: ', end=' ')
    show_position_event(event)
    show_all_events(event)


def on_drag_key(event):
    print('Got left mouse button drag', end=' ')
    show_position_event(event)


def on_double_click(event):
    print('Got double left mouse click: ', end=' ')
    show_position_event(event)
    root.quit()


# Create root window
root = Tk()
label_font = ('courier', 20, 'bold')
widget = Label(root, text='Hello bind world!')
widget.config(bg='red', font=label_font)
widget.config(height=5, width=10)
widget.pack(expand=YES, fill=BOTH)
# Binding mouse events
widget.bind('<Button-1>', on_left_click)
widget.bind('<Button-2>', on_middle_click)
widget.bind('<Button-3>', on_right_click)
widget.bind('<Double-1>', on_double_click)
widget.bind('<B1-Motion>', on_drag_key)
# Binding keyboard events
widget.bind('<KeyPress>', on_key_press)
widget.bind('<Up>', on_arrow_key)
widget.bind('<Return>', on_return_key)
widget.focus()

root.title('Click me!')
root.mainloop()
