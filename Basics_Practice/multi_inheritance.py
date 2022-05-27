# let's check what happens when a child class inherits from 2 parents
class Furniture():
    def __init__(self, name, price, make_time):
        self.name = name
        self.price = price
        self.make_time = make_time

    def build(self):
        print("making furniture for {} in {} days with {}".format(self.name, self.make_time, self.price))

class Floor():
    def __init__(self, make_time, square_feet, price):
        self.make_time = make_time
        self.square_feet = square_feet
        self.price = price

    def building(self):
        print("flooring in progress for {} in {} days with {}".format(self.square_feet, self.make_time, self.price))


class Construct(Furniture, Floor):
    def __init__(self, name, price, make_time, square_feet):
        self.name = super().__init__(name)
        self.price = super().__init__(price)
        self.make_time = super().__init__(make_time)
        #super().__init__(name, price, make_time, square_feet)

small_villa = Construct('venkat', 340000, 100, 1000)
small_villa.build()