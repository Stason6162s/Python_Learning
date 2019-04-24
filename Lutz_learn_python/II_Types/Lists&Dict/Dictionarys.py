print('\t\n Dictionary creating')
D = {}  # empty dict
D = {'name': 'Stas', 'age': 31}  # init dict
print(D)
D = {'food': {'eggs': 2, 'ham': 3}}
print(D)
print(D['food']['ham'])
print('eggs' in D)
# or
D = dict(name='Olya', age=26)
print(D)
print(D['name'])

print('\n\t Methods')
print(D.keys())
print(D.values())
print(D.items())
print(len(D))
D = {x: x * 2 for x in range(10)}
print(D)
L = list(D.keys())
print(L, 'list a keys of dict')
print('\n\t Dictionary change')
D = {'eggs': 1, 'spam': 2, 'ham': 3}
print(D)
D['ham'] = ['grill', 'bake', 'fry']
print(D)
del D['eggs']
print(D)
D['branch'] = 'Bacon'
print(D)
D = {'eggs': 2, 'spam': 1, 'ham': 3}
D2 = {'maffin': 4, 'toast': 5}
D.update(D2)
print(D, 'united dict')

# Table of launguage
print('\n\t Table of language')

table = {
    'Python': 'Guido van Rossum',
    'Perl': 'Larry Wall',
    'Tcl': 'John Ousterhout'
}
langauge = "Perl"
print(table[langauge])
for lang in table.keys():
    print(lang, '\t', table[lang])

# Flexible list
print('\n\t Flexible list')
D = {}
D[99] = 'spam'
print(D)

# Create the sprase data structure

print('\n\t Sprase data structure')
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

X = 2
Y = 3
Z = 4  # value change on incorrect 4>6

print(Matrix[(X, Y, Z)], 'XYZ structure')

try:
    print(Matrix[(2, 3, 6)])
except KeyError:
    print('Errors')

# Using as notes
rec = {}
rec['name'] = "Mike"
rec['age'] = 45
rec['job'] = 'trainer/writer'
print(rec)
# or
mel = {'Series': 'T326', 'Chassis': '062839', 'Sequence': 20171140034, 'ares': ['cpm', 'plastic']}
print(mel.values())

# Dict generators with ZIP()
print('\n\t Dict generators')
Lkeys = ['a', 'b', 'c', 'd']
Lvalues = [2, 3, 4, 5]
D = dict(zip(Lkeys, Lvalues))
print(D, 'zip() methods')
D = {k: v for (k, v) in zip(Lkeys, Lvalues)}
print(D, 'generator to create from zip()')

D = dict.fromkeys(Lkeys, 0)
print(D, '.fromkeys()')
D = {k: 0 for k in Lkeys}
print(D, 'generator from keys list')
D = {k: None for k in 'spam'}
print(D, 'set init values')
# representation of set
D = dict(a=1, b=2, c=3)
print(D)
K = D.keys()
print(K)
print(list(K))
V = D.values()
print(V)
print(list(V))
print(list(D.items()))
print(list(K)[0])
# Sort and sorted for dict

D = dict(a=1, b=4, c=3, d=3)
print(D.keys(), D.values())
Ks = D.keys()
# print(Ks.sort)
Ks = list(Ks)
Ks.sort()
for k in Ks:
    print(k, D[k])
