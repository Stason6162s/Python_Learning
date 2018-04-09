def commas(n):
    digits = str(n)
    assert (digits.isdigit())
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + digits) if result else last3
    return result


def money(n, width=0):
    sign = '-' if n < 0 else ''
    N = abs(n)
    whole = commas(int(N))
    fract = ('%2.f' % N)[:-2]
    format = '%s%s.%s' % (sign, whole, fract)
    return '$%*s' % (width, format)


if __name__ == '__main__':
    def selftest():
        tests = 0, 1
        tests += 12, 123, 1234, 12345, 123456
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))
        print('\t\n')
        for test in tests:
            print('%s [%s]' % (money(test, 17), test))


    import sys

    if len(sys.argv) == 1:
        selftest()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))

