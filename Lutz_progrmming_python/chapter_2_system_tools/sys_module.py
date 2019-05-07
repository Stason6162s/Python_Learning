import sys
import traceback

print('Python %s on %s' % (sys.version, sys.platform))
print(len(dir(sys)))
print(sys.platform, sys.version)
if sys.platform[:3] == 'win':
    print('Hello Windows')
print(sys.path)
print(sys.modules)
print(list(sys.modules.keys()))

try:
    raise TypeError('Already got one')
except TypeError:
    print(sys.exc_info())


def grail(some):
    if some == 'Stan':
        print("My lord")
    else:
        raise TypeError('already got one')


if __name__ == '__main__':
    try:
        grail('arthur')
    except TypeError:
        exc_info = sys.exc_info()
        print(exc_info[0])
        print(exc_info[1])
        traceback.print_tb(exc_info[2])
