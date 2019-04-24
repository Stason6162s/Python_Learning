class rec: pass


rec.name = 'Stas'
rec.age = 31

print(rec.name)

x = rec()
y = rec()

print(x.name, y.name)

x.name = 'Sue'
print(rec.name, x.name, y.name)

print(list(rec.__dict__.keys()))
print(list(x.__dict__.keys()))
print(y.__dict__.keys())
print(x.__class__)

# Add method
print('\t Add method')


def upperName(self):
    return self.name.upper()


print(upperName(x))

rec.method = upperName
print(x.method())
print(y.method())

# print(x.method())
