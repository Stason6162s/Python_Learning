from msvcrt import getch


def on_board_func():
    while True:
        key = ord(getch())
        if key == 27:
            print(f'Pushed the key with number {key}')
            break
        else:
            print(f'Pushed the key with number {key}')


if __name__ == '__main__':
    on_board_func()
