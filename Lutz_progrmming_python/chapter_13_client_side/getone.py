import sys
from ftplib import FTP
from getpass import getpass

non_passive = False
file_name = 'monkeys.jpg'
dir_name = '.'
site_name = 'localhost'
user_info = ('litz', getpass('Pswd?'))
if len(sys.argv) > 1:
    file_name = sys.argv[1]

print('Connecting....')
connection = FTP(site_name)
connection.login(*user_info)
connection.cwd(dir_name)
if non_passive:
    connection.set_pasv(False)

print('Downloading....')
local_file = open(file_name, 'wb')
connection.retrbinary('RETR' + file_name, local_file.write, 1024)
connection.quit()
local_file.close()

if input('Open file') in ['Y', 'y']:
    print('Playing file')
