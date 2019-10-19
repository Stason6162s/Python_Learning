class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def __str__(self):
        return '%s => %s' % (self.__class__.__name__, self.name)

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)


if __name__ == '__main__':
    anton = Person('Anton Kobeshev', 32, 63000, 'Techician')
    jonie = Person('Evgeniy Zolotuchin', 35, 63000)
    print(anton.last_name())
    jonie.give_raise(.10)
    print(jonie.pay)
    print(anton)
