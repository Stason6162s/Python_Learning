class Super:
    def method(self):
        print('I am Super.method')

    def delegate(self):
        self.action()


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('I am Replacer.method')


class Extender(Super):
    def method(self):
        print('Starting Extended.method')
        Super.method(self)
        print('Ending Extended.method')


class Provider(Super):
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + ' ...')
        klass().method()
    print('\nProvider')
    x = Provider()
    x.delegate()


