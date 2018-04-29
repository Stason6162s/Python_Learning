class General(Exception): pass


class Specific1(General): pass


class Specific2(General): pass


def rasier():
    x = General()
    raise x


def raiser1():
    x = Specific1()
    raise x


def raiser2():
    x = Specific2()
    raise x


for funk in (rasier, raiser1, raiser2):
    try:
        funk()
    except General as X:
        import sys

        print('caught', sys.exc_info())
        print('caught', X.__class__)
