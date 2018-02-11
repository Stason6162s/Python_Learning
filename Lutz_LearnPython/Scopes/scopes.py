import builtins

# global scope
X = 99


def func(Y):
    # local scope
    Z = X + Y
    return Z


print(func(4))

print(dir(builtins))


def func1():
    X = 88


func1()
print(X)


# or

def funk2():
    global X
    X = 122


funk2()
print(X)

# more difficult

y, z = 1, 2


def all_global():
    global x
    x = y + z

