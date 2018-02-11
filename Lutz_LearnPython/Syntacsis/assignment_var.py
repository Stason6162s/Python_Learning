import sys

Spam_1 = 'spam'
print(Spam_1)
_spam = 'SPAM'
log = open('data.dat', 'a')
while True:
    reply = input('For stop, print \" STOP\"')
    if reply == 'stop': break
    print(_spam, Spam_1, sep='|')
    print(_spam, Spam_1, sep=', ', end='...\n')
    print(_spam, Spam_1, sep=' | ', end='!\n')
    print(_spam, Spam_1, sep=' | ', end='!\n', file=log)
print('%s: %s' % ('Your', 'finish'))


# class FileFaker:
#     def write(self, string):
#         string.Upper()
#         print(string)
#
#
# sys.stdout = FileFaker()
# print('Stas')
