'''
class Vehicle:
    def __init__(self, name, purchase_year):
        self.name = name
        self.purchase_year = purchase_year

    def start(self):
        print("vehicle started")

class Car(Vehicle):
    def __init__(self, name, company):
        self.company = company
        super().__init__(name)

    def start(self):
        print("car started")

class Lorry(Vehicle):
    def __init__(self, company, name, purchase_year):
        self.company = company
        super().__init__(name, purchase_year)

    def start(self):
        print("Lorry started")

    def health_check(self):
        print("health okay")

class Audi(Car):
    def __init__(self, year, model, name):
        self.year = year
        self.model = model
        super().__init__(name)

    def car_details(self):
        print("it's audi {} from {}".format(self.model, self.year))

class Registration(Car, Lorry):
    def __init__(self, company, name, purchase_year):
        super().__init__(name, company, purchase_year)

    def start(self):
        print("registration in progress for vehicle {} from company {}". format(name, company))

reg = Registration("venkat", "Benz", 1999)
reg.start()
'''
class First():
    def __init__(self):
        super().__init__()
        print("first")

class Second():
    def __init__(self):
        super().__init__()
        print("second")

class Third(First, Second):
    def __init__(self):
        super().__init__()
        print("third")
Third()
print(Third.__mro__)