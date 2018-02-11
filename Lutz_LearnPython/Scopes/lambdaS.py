"""
How to use lambda
"""
Y = None


def func():
    x = 4
    action = (lambda n: x ** n)
    return action


def test(value):
    action = (lambda n: value + n)
    return action


Y = func()
print(Y(2))

Z = test(8)
print(Z(2))


# except from lambda

def makeActionNotWork():
    act = []
    for i in range(5):
        act.append(lambda x: i + x)
    return act


act = makeActionNotWork()
print(act[0])


def makeActionWork():
    act = []
    for i in range(5):
        act.append(lambda x, i=i: i ** x)
    return act


act = makeActionWork()
print(act[0](2))
