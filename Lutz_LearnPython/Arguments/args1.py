def f(a):
    a = 99


b = 88
f(b)
print(b)


def changer(a, b):
    a = 1
    b[0] = 'spam'


X = 1
L = [1, 2]

changer(X, L)
print(X, L)


def f(a, b, c): print(a, b, c)


def info(name, age, job): print('name is: ' + name + ', age : ' + str(age) + ', job is :' + job)


f(1, 2, 3)

f(c=2, a=3, b=1)

info('PLC', 'Stas', '31')
info(name='Stas', job='PLC', age=31)


def G(*args): print(args)


G()
G(1)
G(1, 2, 3)


def dictF(**args): print(args)


dictF()
dictF(a=1, b=2)


def collectArgs(arg, *pargs, **kargs): print(arg, pargs, kargs)


collectArgs(1, 2, 3, x=4, y=5)


