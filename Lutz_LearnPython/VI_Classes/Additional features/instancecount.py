class Spam:
    numInstance = 0

    def count(cls):
        cls.numInstance += 1

    def __init__(self):
        self.count()

    count = classmethod(count)


class Sub(Spam):
    numInstance = 0

    def __init__(self):
        Spam.__init__(self)


class Other(Spam):
    numInstance = 0


x, x1 = Spam(), Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(), Other()

print(x.numInstance)
print(y1.numInstance)
print(z1.numInstance)
