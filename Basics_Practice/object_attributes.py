class Vehicle():
    def __init__(self, company, transmission, cc):
        self.company = company
        self.transmission = transmission
        self.cc = cc


car = Vehicle('Tata', 'Auto', 1600)
print(car.__dict__)  # use inbuilt dict method on instance to get key value pairs
print(vars(car))  # call var function on instance to get key value pairs
for keys, values in car.__dict__.items():
    print(keys, ':', values)

print(Vehicle.__dict__)  # calling class attributes instead of instance attributes
