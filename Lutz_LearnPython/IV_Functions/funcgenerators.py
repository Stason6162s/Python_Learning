# 3.Functions-generators
print('\t\n Func-generators')


def gensquare(N):
    for i in range(N):
        yield i ** 2


for i in gensquare(5):
    print(i, end=' / ')
func = gensquare(5)
print(func)
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print('\t\n Expression-generators')
# Expression-generator

# Simple list-generator
print([x ** 2 for x in range(5)])
# Expression

print(list(x ** 2 for x in range(5)))
print('\t OR')
G = (x + 1 for x in range(5))
print(next(G))
print(next(G))
print(G.__next__())
print(G.__next__())
# Example
for num in (x ** 2 for x in range(5)):
    print('%s, %s' % (num, num / 2.0))

G = (c * 2 for c in 'stas')
print(list(G))


def times_two(S):
    for c in S:
        yield c * 2


C = times_two('Spam')
print(list(C))
