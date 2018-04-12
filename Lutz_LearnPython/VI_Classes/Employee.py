class Employee:
    def __init__(self, how_mach):
        self.salary = how_mach

    def compute_salary(self):
        print(self.salary)

    def give_raise(self): pass

    def promote(self): pass

    def retire(self): pass


class Engineer(Employee):
    def compute_salary(self):
        print(self.salary * 0.1)


bob = Employee('1000')  # Base behavior
greg = Engineer('1000')  # Override behavior

