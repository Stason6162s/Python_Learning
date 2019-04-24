x = set('abcd')
y = set('xyzcd')

print(x, y)
print('e' in x)
print('d' in x)
print(x | y)
z = x.intersection(y)
print(z)
z.add('spam')
print(z)

for item in set('abcd'): print(item * 3)

# how it work in 3.0 python

print(set([1, 2, 3, 4]))  # old method set multiplicity

print({1, 2, 3, 4})
S = set()
S.add(1.23)
print(S)

L = [1, 2, 1, 3, 4, 5, 5]
S = set(L)  # convert to multiplicity
print(S)
L = list(set(L))  # convert to list
print(L)

# using multiplicity in work with DB

engineers = {'bob', 'sue', 'ann', 'vic'}
manager = {'sue', 'ken', 'tom'}

print('bob' in engineers)

print(engineers & manager)
print(engineers | manager)
print(engineers - manager)
print(manager - engineers)

