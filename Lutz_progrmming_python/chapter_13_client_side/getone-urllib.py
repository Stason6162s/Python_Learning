#! /usr/local/bin/python

from urllib.request import urlopen

print('Begin...')

file_name = 'Monkey.txt'
remote_address = f'file:///C://Trash//{file_name}'

print(f'Downloading {remote_address}')

# or
# urllib.request.urlretrieve(remote_address, file_name)

remote_file = urlopen(remote_address)
print(str(remote_address))
local_file = open(file_name, 'wb')
local_file.write(remote_file.read())
local_file.close()
remote_file.close()
print('Download completed')
