class SkipIterartor:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.ofset = 0

    def __next__(self):
        if self.ofset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.ofset]
            self.ofset += 2
            return item


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterartor(self.wrapped)


if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))

    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
