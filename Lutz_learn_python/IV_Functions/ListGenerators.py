print(ord('S'))

res = []
for x in 'Spam':
    res.append(ord(x))
print(res)

resp = []
resp = map(ord, 'stas')
print(list(resp))

resgen = [ord(x) for x in 'stas']
print(resgen)

print([x ** 2 for x in range(10)])
print([x ** 2 for x in range(10) if x % 2 == 0])
print([x * y for x in range(1, 10) for y in range(1, 11)])
