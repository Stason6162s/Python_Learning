import sys
import os
import time
import _thread as thread

from socket import *

BLOCK_SIZE = 1024
HOST = 'localhost'
PORT = 9000

help_text = """
Usage...
server => getfile.py -mode server [-port nnn] [-host hhh | localhost]
client => getfile.py [-mode client] -file fff [-port nnn] [-host hhh | localhost]
"""


def now():
    return time.asctime()


def parse_command_line():
    dict = {}
    args = sys.argv[1:]
    while len(args) >= 2:
        dict[args[0]] = args[1]
        args = args[2:]
    return dict


def client(host, port, filename):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send((filename + '\n').encode())
    drop_dir = os.path.split(filename)[1]
    file = open(drop_dir, 'wb')
    while True:
        data = sock.recv(BLOCK_SIZE)
        if not data:
            break
        file.write(data)
    sock.close()
    file.close()
    print(f'{now()} Client got {filename}')


def server_thread(client_sock):
    sock_file = client_sock.makefile('r')
    file_name = sock_file.readline()[:-1]

    try:
        file = open(file_name, 'rb')
        while True:
            bytes = file.read(BLOCK_SIZE)
            if not bytes:
                break
            sent = client_sock.send(bytes)
            assert sent == len(bytes)
    except:
        print(f'Error downloading file on server {file_name}')
    client_sock.close()


def server(host, port):
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind((host, port), )
    server_sock.listen(5)

    while True:
        client_sock, client_address = server_sock.accept()
        print(f'{now()} Server connected by {client_address}')
        thread.start_new_thread(server_thread, (client_sock,))


def main(args):
    host = args.get('-host', HOST)
    port = int(args.get('-port', PORT))

    if args.get('-mode') == 'server':
        if host == 'localhost':
            host = ''
        server(host, port)
    elif args.get('-file'):
        client(host, port, args['-file'])
    else:
        print(help_text)


if __name__ == '__main__':
    args = parse_command_line()
    main(args)
