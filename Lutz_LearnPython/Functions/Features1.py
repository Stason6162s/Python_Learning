def times(x, y):
    return x * y


now = times(2, 4)
print(now)
now = times(3.14, 2)
print(now)
now = times('Ni', 4)
print(now)


def interseq(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


print(interseq('stas', 'spam'))
print(interseq([1, 2, 3, 4], (1, 7, 6, 4 )))

