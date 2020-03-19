import socketserver, time

HOST = ''
PORT = 9000


def now():
    return time.ctime(time.time())


class MyClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address, now())
        time.sleep(5)
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            reply = f'Echo => {now()} : {data}'
            self.request.send(reply.encode())
        self.request.close()

my_addr = (HOST, PORT)
server = socketserver.ThreadingTCPServer(my_addr, MyClientHandler)
server.serve_forever()