"""
mydir.py Выводит содержание других модулей
"""
seplen = 60
sepchr = '-'


def listinig(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name: ', module.__name__, 'file: ', module.__file__)
        print(sepline)
    count = 0
    for attr in module.__dict__:  # Сканируем пространство имен модуля
        print("%02d) %s" % (count, attr), end=' ')
        if attr.startswith('__'):
            print("<built-in name>")  # Пропустить __file__ и т.д.
        else:
            print(getattr(module, attr))  # То же, что и .__dict__[attr]
        count += 1

    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)
        print(sepline)


if __name__ == '__main__':
    import mydir

    listinig(mydir)
