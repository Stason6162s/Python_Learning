

# Use the def function


def f1(x): return x ** 2


def f2(x): return x ** 3


def f3(x): return x ** 4


L_def = [f1, f2, f3]

for f in L_def:
    print(f(2))

# or using lambda

L_lambda = [
    lambda x: x ** 2,
    lambda x: x ** 3,
    lambda x: x ** 4
]

for f in L_lambda:
    print(f(4))
