from VI_Classes.classtools import AttrDisplay


class Person(AttrDisplay):
    """
    Create and processes records about peoples
    """

    def __init__(self, name, job=None, pay=0):  # __init__ it is CONSTRUCTOR of class
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):  # Family must to be written
        return self.name.split()[-1]  # in the end of record

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))  # percent - it's value in range 0..1

    # def __str__(self):
    #     return 'Employee: %s, %s' % (self.name, self.pay)


class Manager(Person):
    """ To extending and overriding class Person with adapted functions """

    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    # Wrong way to extend the methods 'give_raise()'
    # def give_raise(self, percent, bonus=.10):
    #     self.pay = (self.pay * (1 + percent + bonus))

    # Right way to extend the method 'give_raise()'
    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raise(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    stas = Person("Stas Alekseev")
    pasha = Person('Pawel Koznov', job='Master', pay=70000)
    print(stas.name, stas.pay)
    print(stas)
    print(pasha.name, pasha.pay)
    print(pasha)
    print(stas.last_name(), pasha.last_name())
    pasha.give_raise(.05)
    print(pasha.pay)

    print('\t Management')
    griga = Manager('Grigoriy Belyaev', 150000)
    print(griga)
    griga.give_raise(.10)
    print(griga)

    print('\ Polymorphism in action ')
    for object in (pasha, stas, griga):
        object.give_raise(.10)
        print(object)

    print('\t Department')
    pe_department = Department(pasha, stas)
    pe_department.add_member(griga)
    pe_department.give_raise(.05)  # Add rise to all
    pe_department.show_all()
