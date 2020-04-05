import sys
import os

import urllib.request
import urllib.parse

print('Hi there!')
print(f'{sys.argv=}')
try:
    server_name, file_name = sys.argv[1:3]
except:
    server_name, file_name = 'learning-python.com', '/index.html'

remote_address = f'http://{server_name}{file_name}'

if len(sys.argv) == 4:
    local_name = sys.argv[3]
else:
    (scheme, server, path, parms, query, frag)= urllib.parse.urlparse(remote_address)
    local_name = os.path.split(path)[1]

print("\tI'm here", remote_address, local_name)
urllib.request.urlretrieve(remote_address, local_name)
remote_data = open(local_name, 'rb').readlines()
for line in remote_data[:16 ]:
    print(line)