L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10
print(L)
# or, to use generator
L = [x + 10 for x in L]
print(L)

file = open('script1.py')
lines = file.readlines()
print(lines)

lines = [line.rstrip() for line in lines]
print(lines)

lines = [line.upper() for line in open('script1.py')]
print(lines)

lines = [line.rstrip().upper() for line in open('script1.py')]
print(lines)

lines = [line.split() for line in open('script1.py')]
print(lines)

lines = [line.replace(' ', '!') for line in open('script1.py')]
print(lines)

# more difficult generator
data = [line.rstrip() for line in open('script1.py') if line[0] == 'p']
print(data)

# all generation may be released how FOR, example
res = []
for line in open('script1.py'):
    if line[0] == 'p':
        res.append(line.rstrip())
print(res)
D = dict(enumerate('spam'))
print(D)


# *arg context
def f(a, b, c, d):
    print(a, b, c, d, sep='&')


print(f(1, 2, 3, 4))
print(f(*[11, 12, 13, 14]))
print(f(*open('script1.py')))