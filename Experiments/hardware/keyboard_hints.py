import time
from msvcrt import getch

import keyboard


def on_board_func():
    while True:
        key = ord(getch())
        if key == 27:
            break
        else:
            print(f'Pushed the {chr(key)} keys with number {key}')


def using_keyboard():
    while True:
        key = keyboard.get_hotkey_name()
        if key == 'esc':
            print(f'Pushed the {keyboard.get_hotkey_name()}')
            break
        else:
            if key != '':
                print(f'Pushed the {key} button')
                time.sleep(1)


if __name__ == '__main__':
    using_keyboard()
