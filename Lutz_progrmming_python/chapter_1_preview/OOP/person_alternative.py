class Person:
    """
    The universal representation of human and logic
    """

    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '%s => %s' % (self.__class__.__name__, self.name)


class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'Manager')

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    antony = Person('Anton Kobeshev', 32, 63000, 'Techician')
    print(antony)
    antony.give_raise(10)
    print(antony.pay)
    artem = Manager('Artem Syrkov', 45, 150000)
    print(artem)
    for obj in (antony, artem):
        obj.give_raise(.10)
        print(obj, obj.pay)
