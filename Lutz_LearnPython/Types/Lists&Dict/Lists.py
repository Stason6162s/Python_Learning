L = []
L = [1, 2, 3, 4]
Lm = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for c in Lm:
    print(c)
res = [c * 2 for c in 'SPAM']
print(res)
res.append('eggs')
print(res)
res.sort()
print(res)

# sort and sorted
print('\t \n .sort and sorted()')
L = ['abc', 'ABD', 'aBe']
print(L)
L.sort()
print(L)
L.sort(key=str.lower)
print(L)
L.sort(key=str.lower, reverse=True)
print(L)
L = ['abc', 'ABD', 'aBe']
M = sorted(L, key=str.lower, reverse=True)
print(M)
X = sorted([x.lower() for x in L])
print(X)

# extend() and pop()
print('\t \n .extend(), .pop(), .reverse() and reversed(L) ')
L = list('12')
print(L)
L.extend([3, 4, 5])
print(L, 'extend()')
L.pop()
print(L, 'pop()')
L.reverse()
print(L, 'reverse()')
print(list(reversed(L)), 'reversed()')
print('\t\n .index(), .insert(), .remove(), .pop(index)')
L = ['ham', 'eggs', 'spam']
print(L.index('eggs'), '.index()')
L.insert(1, 'toast')
print(L, '.insert()')
L.remove('spam')
print(L, 'remove()')
L.pop(1)
print(L, '.pop(index)')
print('\t\n del()')
L = [1, 2, 3, 4, 5]
del L[0]
print(L, 'del L[index]')
del L[2:]
print(L, 'del L[:]')
