import time
from socket import *

my_host = ''  # ПК на котором выполняется скрипт
my_port = 9000  # любой кроме зарезервированных 0-1023

# AF_INET/SOCK_STREAM - объект протокола TCP/IP, обычно по умолчанию, но указывают явно
socket_object = socket(AF_INET, SOCK_STREAM)
# привязка объекта socket к адресу ПК
socket_object.bind((my_host, my_port))
# кол-во запросов в очереди до того как сервер начнет их отклонять
socket_object.listen(5)

while True:
    print(f'{time.ctime(time.time())} Server {my_host} is running')
    '''
    Ждет поступления от клиента запроса на соединение. Соединение осуществляется
    через socket_object, но связь с клиентом происходит через новый сокет conn
    '''
    connection, address = socket_object.accept()

    print(f'{time.ctime(time.time())} Server connections by {address}')

    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.send(b'ECHO=>' + data)
    connection.close()
