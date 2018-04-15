class Wrapper:
    def __init__(self, object):
        self.wrapper = object

    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapper, attrname)


if __name__ == '__main__':
    x = Wrapper([1, 2, 3])
    x.append(4)
    print(x.wrapper)
