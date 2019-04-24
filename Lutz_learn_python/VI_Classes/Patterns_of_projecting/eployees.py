class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return '<Employee: name = %s, salary = %s>' % (self.name, self.salary)

    def give_raise(self, percent):
        self.salary += (self.salary * percent)

    def work(self):
        print(self.name, 'does stuff')


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, ' makes food')


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, ' interfaces with customers')


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, 'makes pizza')


if __name__ == '__main__':
    bob = PizzaRobot('Bob')
    print(bob)
    bob.work()
    bob.give_raise(.20)
    print(bob)
    print()
    for klass in (Employee, Chef, Server, PizzaRobot):
        obj = klass(klass.__name__)
        obj.work()
