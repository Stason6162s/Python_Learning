import socket

def test(host = 'localhost'):
	host = socket.gethostbyname(host)
	print(host)

if __name__ == '__main__':
	test('EU-ST-05032')