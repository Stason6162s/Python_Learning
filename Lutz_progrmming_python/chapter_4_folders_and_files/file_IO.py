import os

file = open('data.txt', 'w')
file.writelines(os.listdir())
file.close()

with open('with.dat', 'a') as file:
    for item in os.popen('dir /B').read():
        file.write(item)

for line in open('with.dat'):
    print(line)

open('data.bin', 'wb').write(b'Spam\n')
print(open('data.bin', 'rb').read())
