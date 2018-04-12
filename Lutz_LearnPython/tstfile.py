from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass


# X=Super()

class Sub(Super):
    def action(self): print('spam')


X = Sub()
X.delegate()