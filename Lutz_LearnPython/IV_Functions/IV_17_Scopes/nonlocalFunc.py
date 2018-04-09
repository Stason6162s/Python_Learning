def tester(start):
    state = start

    def nested(label):
        print(label, state)

    return nested


F = tester(0)
print(F('spam'))
print(F('ham'))


# This not work
def tester1(start):
    state = start

    def nested(label):
        print(label, state)
        state += 1  # error

    return nested


F = tester(0)
print(F('spam'))


#  use nonlocal

def tester2(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1

    return nested


F = tester2(1)
print(F('spam'))
print(F('eggs'))
print(F('ham'))


def tester4(start):
    """
    Use atribute of function for save data
    """
    def nested(label):
        print(label, nested.state)
        nested.state += 1

    nested.state = start
    return nested


F = tester4(0)
F('man')
G = tester4(42)  # be careful, i use the wrong function and didn't give result
G('woman')
G('girl')
print(G.state)
print(tester4.__doc__)
