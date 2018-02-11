def min1(*args):
    res = args[0]
    for arg in args[1:0]:
        if arg < res:
            res = arg
            return res


x = min(3, 42, 2, 1, 3)
print(x)


def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first


print(min2('aa', 'cc'))


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]


print(min3([2, 2], [3, 3], [4, 4]))


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y): return x < y


def grtrthan(x, y): return x > y


print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))
