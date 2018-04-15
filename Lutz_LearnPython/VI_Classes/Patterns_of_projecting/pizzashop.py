from VI_Classes.Patterns_of_projecting.eployees import PizzaRobot, Server


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, 'order from', server)

    def pay(self, server):
        print(self.name, 'pays for item to', server)


class Oven:
    def bake(self):
        print('Oven bakes')


class PizzaShop:
    def __init__(self,name):
        self.server = Server('Pat')
        self.chief = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chief.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    scene = PizzaShop('Pizza-Zyza')
    scene.order('Harry')
    scene.order('Shagy')

