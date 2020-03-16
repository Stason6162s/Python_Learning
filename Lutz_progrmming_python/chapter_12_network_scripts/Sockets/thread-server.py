import time
import _thread as thread

from socket import *

HOST = ''
PORT = 9000

socket_obj = socket(AF_INET, SOCK_STREAM)
socket_obj.bind((HOST, PORT))
socket_obj.listen(5)


def now():
    return time.ctime(time.time())


def handle_client(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        reply = f'{now()} Echo => {data} '
        connection.send(reply.encode())


def dispatcher():
    while True:
        connection, address = socket_obj.accept()
        print(f'Server connected by {address}')
        print(f'at {now()}')
        thread.start_new_thread(handle_client, (connection,))


dispatcher()
