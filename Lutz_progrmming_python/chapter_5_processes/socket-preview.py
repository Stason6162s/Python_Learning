from socket import socket, AF_INET, SOCK_STREAM

PORT = 5008
HOST = 'localhost'


def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(("", PORT))
    sock.listen(5)
    while True:
        conn, address = sock.accept()
        data = conn.recv(1024)
        reply = f'server got: [{data}]'
        conn.send(reply.encode())


def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send(name.encode())
    reply = sock.recv(1024)
    sock.close()
    print(f'client got: [{reply}]')


if __name__ == '__main__':
    from threading import Thread

    server_thread = Thread(target=server)
    server_thread.daemon = True
    server_thread.start()
    for i in range(5):
        Thread(target=client, args=('client_%s'% i,)).start()
