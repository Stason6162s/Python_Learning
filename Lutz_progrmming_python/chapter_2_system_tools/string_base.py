import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.whitespace)

if __name__ == '__main__':
    count = 0
    for char in string.ascii_letters[:26]:
        count += 1
        print('#define:%s_%d ' % (char, count))

    delim = 'Ni'
    joint_string = delim.join(['aaa', 'bbb', 'ccc'])  # join string from lists
    print(joint_string)
    # String remade to chars array
    chars = list('Loretta')
    print(chars)
    chars.append('!')
    print(''.join(chars))
    # Converted
    print(type(int('42')), type(eval('42')))
    print(type(str(42)), type(repr(42)))
    # Operator and method of formatting
    print('This %d operator of converting to string' % 42)
    print('And this {:d} method of converting to string'.format(42))
    print('Or this {0} method of converting to string with positional argument'.format(42))
