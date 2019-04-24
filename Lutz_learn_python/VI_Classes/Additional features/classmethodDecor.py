def count(aClass):
    aClass.numInstance = 0
    return aClass


@count
class Spam:

    def __init__(self):
        Spam.numInstance += 1

    def printNumInstance(cls):
        print("Num instance :", cls.numInstance)

    printNumInstance = classmethod(printNumInstance)


if __name__ == '__main__':
    a, b = Spam(), Spam()  # classmethod use instead staticmethod
    a.printNumInstance()
    Spam.printNumInstance()
