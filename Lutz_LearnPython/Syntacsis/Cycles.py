print('\n\t Cycles')
print('\t Cycle WHILE X:')
C = 0
while C <= 9:
    print(C, end=', ')
    C += 1
else:
    print('Cycle Finished')
x = 'spam'
# while for string data
while x:
    print(x, end=' | ')
    x = x[1:]

print('\n')


def emptyFunc():
    ...


def newFunc():
    pass


x = 10
while x:
    x -= 1
    if x % 2 != 0:
        continue
    print(x, end='/ ')
print('\t Cycles FOR:')
for x in ['spam', 'eggs', 'toast']:
    print(x)
# sum
sum = 0
for x in [1, 2, 3, 4]:
    sum += x
print(sum)
# prod
prod = 1
for x in [1, 2, 3, 4]: prod *= x
print(prod)

# assignment tuple in cycle for
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)
# iterators dict in for
D = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for key in D:
    print(key, ' => ', D[key])
print(list(D.items()))

for (key, value) in D.items():
    print(key, ' => ', value)
# or

print(T)

for both in T:
    a, b = both
    print(a, b)

items = ['aaa', 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]
for keys in tests:
    for item in items:
        if keys == item:
            print(keys, 'was found')
            break
    else:
        print(keys, ' not found')
# bypass part of collection
S = 'asdfghjkl'
for x in range(0, len(S), 2): print(S[x], end=' ')
print('\n')
# enumerate
S = 'Stason'
E = enumerate(S)
for x in range(0, len(S)):
   print(next(E))