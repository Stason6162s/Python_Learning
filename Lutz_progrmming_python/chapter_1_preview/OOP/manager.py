# TODO Why importing of modules requires the full path to the module?
from Lutz_progrmming_python.chapter_1_preview.OOP.person import Person


class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, self.__class__.__name__)

    def give_raise(self, percent, bonus=0.1):
        # self.pay *= (1.0 + percent + bonus)
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    artem = Manager('Artem Surkov', 40, 130000)
    print(artem.last_name())
    artem.give_raise(.20)
    print(artem.pay)
    print(artem)
    print(artem.job)
