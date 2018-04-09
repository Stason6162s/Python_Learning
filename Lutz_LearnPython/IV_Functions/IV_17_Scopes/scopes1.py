# X = 99


# def f1():
#     X = 88
#
#     def f2():
#         print(X)
#
#     f2()
#
#
# f1()

# or
#
# def f1():
#     X = 88
#
#     def f2():
#         print(X)
#
#     return f2
#
#
# action = f1()
# action()


# fabric function

def marker(N):
    def action(X):
        return X ** N

    return action


f = marker(2)
print(f)
print(f(3))
print(f(4))

g = marker(3)
g(2)
print(g(4))
