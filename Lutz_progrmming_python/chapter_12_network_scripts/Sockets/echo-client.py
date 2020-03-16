import sys
import os
from socket import *

server_host = 'localhost'
server_port = 9000

username = os.getlogin()

# message = [b'Hello network world']
message = [username.encode()]

if len(sys.argv) > 1:
	server_host = sys.argv[1]
	if len(sys.argv) > 2 :
		message = (x.encode() for x in sys.argv[2:])

socket_obj = socket(AF_INET, SOCK_STREAM)
socket_obj.connect((server_host, server_port))

for line in message:
	socket_obj.send(line)
	data = socket_obj.recv(1024)
	print(f'Client received {data}')
socket_obj.close()