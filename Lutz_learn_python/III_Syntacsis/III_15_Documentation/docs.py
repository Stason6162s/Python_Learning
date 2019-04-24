import sys

print(dir(sys), end='\n')
print(dir([]))
print(dir(''))
print(list(dir([])))
print('\n')
print(sys.__doc__)
print(int.__doc__)
help(sys.getrefcount)
help(sys)
