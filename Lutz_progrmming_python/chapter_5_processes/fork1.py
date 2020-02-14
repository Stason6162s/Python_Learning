import os


def child():
    print(f'Hello from child, PID: {os.getpid()}')
    os._exit(0)


def parent():
    while True:
        new_pid = os.fork()
        if new_pid == 0:
            child()
        else:
            print(f'Hello from parent {os.getpid()} {new_pid}')
        if input() == 'q':
            break


parent()
