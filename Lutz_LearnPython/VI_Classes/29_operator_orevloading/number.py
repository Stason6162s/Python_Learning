class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)

    def __str__(self):
        return 'Value .data: %s' % self.data


X = Number(5)
Y = X - 3
print(Y.data)
print(Y)
print('\t __getitem__ and __setitem__')


# class Indexer:
#     def __getitem__(self, item):
#         return item ** 2


class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem', index)
        return self.data[index]


Z = Indexer()
print(Z[:-3])
