# recurse


def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])


def mySum1(L):
    return 0 if not L else L[0] + mySum1(L[1:])


def mySum1(L):
    first, *rest = L
    return first if not rest else first + mySum1(rest)


L = [1, 2, 3, 4, 5]

#   print(mysum(L))
print(mySum1(L))
print(mySum1(L))


# annotations

def mySum3(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c

print(mySum3(1,2,3))
print(mySum3.__annotations__)