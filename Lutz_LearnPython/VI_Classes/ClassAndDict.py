rec = {}
rec['name'] = 'Pavel'
rec['age'] = 27
rec['job'] = 'master/technician'

print(rec['name'])


class Rec: pass


Rec.name = 'Pawel'
Rec.age = 27
Rec.job = 'master/technician'

print(Rec.name)

person = Rec()

person.name = "Pawel"
person.age = 27
person.job = 'master/technician'

person2 = Rec()


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def info(self):
        return (self.name, self.job)


pers1 = Person('Stas', 'PLC')
pers2 = Person('Sergey', 'Master')

print(pers1.name, pers2.info())
