class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

x.setdata("King Arthur")
y.setdata(0.2994)

x.display()
y.display()

z = FirstClass()
z.data = 'New Vegas'
z.display()


class SecondClass(FirstClass):
    def display(self):
        print("Current value = %s " % self.data)


w = SecondClass()
w.data = 'Current value'
w.display()


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass('Satan')
print(a)
a.display()
b=a+'666'
b.display()
print(b)
a.mul(3)
a.display()