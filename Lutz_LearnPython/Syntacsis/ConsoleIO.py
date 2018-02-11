while True:
    reply = input('Enter text : ')
    if reply == 'stop': break
    print(reply.upper())
print('\n\t Bye %s' % reply)

# Isdigit
print('\n\t Check for digit')
while True:
    reply = input('Your value, numbers only:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('\t You input the wrong symbol: ' + reply + '\n')
    else:
        print(int(reply) * 2)
print('\n\t Bye-bye')

# with TRY/EXCEPT
print('\n\t Using try/except instruction')
while True:
    reply = input('Enter num: ')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Wrong type of data')
    else:
        print(int(reply) ** 2)
print('End try/except cycle')
