class Spam:
    numInstance = 0

    def __init__(self):
        Spam.numInstance += 1

    def print_NumInstance():
        print('Numbers of instance: ', Spam.numInstance)

    print_NumInstance = staticmethod(print_NumInstance)


class Sub(Spam):
    def print_NumInstance():
        print("Extra stuff:")
        Spam.print_NumInstance()

    print_NumInstance = staticmethod(print_NumInstance)


class Other(Spam):
    pass


if __name__ == '__main__':
    a = Spam()
    b = Spam()
    c = Spam()
    Spam.print_NumInstance()
    a.print_NumInstance()
    x = Sub()
    y = Sub()
    Sub.print_NumInstance()
    y.print_NumInstance()
    foo = Other()
    foo.print_NumInstance()