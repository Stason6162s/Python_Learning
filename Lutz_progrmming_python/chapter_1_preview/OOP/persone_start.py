class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job


if __name__ == '__main__':
    anton = Person('Anton Kobeshev', 32, 63000, 'Techician')
    jonie = Person('Evgeniy Zolotuchin', 35, 63000)
    print(anton.name.split()[-1])
    jonie.pay *= 1.10
    print(jonie.pay)
