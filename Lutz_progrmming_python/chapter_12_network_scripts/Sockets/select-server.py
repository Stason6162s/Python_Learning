"""
Сервер обслуживает параллельно несколько клиентов с помощью select.
"""

import sys
import time
from select import select
from socket import socket, AF_INET, SOCK_STREAM

HOST = ""
PORT = 9000

if len(sys.argv) == 3:
    HOST, PORT = sys.argv[1:]

number_port_sockets = 2


def now():
    return time.ctime(time.time())


# Создаем главные сокеты для приема новых запросов на соединение от клиентов
main_socks, read_socks, write_socks = [], [], []
for sock in range(number_port_sockets):
    port_sock = socket(AF_INET, SOCK_STREAM)
    port_sock.bind((HOST, PORT))
    port_sock.listen(5)
    main_socks.append(port_sock)
    read_socks.append(port_sock)
    PORT += 1

# цикл событий: слушать и мультиплесировать, пока процесс не завершится
print('select-server loop starting')
while True:
    read_ables, write_ables, exceptions = select(read_socks, write_socks, [])
    for socket_obj in read_ables:
        if socket_obj in main_socks:
            new_sock, address = socket_obj.accept()
            print(f'Connect : {address} {id(new_sock)}')
            read_socks.append(new_sock)
        else:
            data = socket_obj.recv(1024)
            print(f'\tGot {data} on {id(socket_obj)}')
            if not data:
                socket_obj.close()
                read_socks.remove(socket_obj)
            else:
                reply = f"{now()} Echo = > {data}"
                socket_obj.send(reply.encode())
