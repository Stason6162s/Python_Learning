'''
Utilities and tools for work with any class
'''


class AttrDisplay:
    def gather_attribute(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s = %s ' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        return '[%s, %s]' % (self.__class__.__name__, self.gather_attribute())


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attribute1 = TopTest.count
            self.attribute2 = TopTest.count + 1
            TopTest.count += 2


    class SecondTest(TopTest):
        pass


    X, Y = TopTest(), SecondTest()

    print(X)
    print(Y)
