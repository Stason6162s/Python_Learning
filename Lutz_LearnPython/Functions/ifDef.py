a = input('Input a: ')
b = input('Input b: ')
if a > b:
    def func():
        return int(a) - int(b)
else:
    def func():
        return int(a) + int(b)

print(func())
