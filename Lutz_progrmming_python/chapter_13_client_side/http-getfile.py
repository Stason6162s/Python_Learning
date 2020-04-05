import sys
import http.client
show_lines=6

try:
    server_name, file_name = sys.argv[1:]
except:
    server_name, file_name = 'learning-python.com', 'index.html'

    print(server_name, file_name)
    server = http.client.HTTPConnection(server_name)
    server.putrequest('GET', file_name)
    server.putheader('Accept', 'text/html')
    server.endheaders()

    reply = server.getresponse()
    if reply.status != 200:
        print(f'Error sending request, {reply.status}, {reply.reason}')
    else:
        data = reply.readlines()
        reply.close()
        for line in data[:show_lines]:
            print(line)
