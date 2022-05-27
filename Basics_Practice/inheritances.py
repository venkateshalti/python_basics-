# This is a demonstration of inheritance where Vehicle class has a child class named Car inheriting attributes and methods from it
class Vehicle:  # parent or base class, very generic
    owner = "Venki"  # this is a class variable, not instance specific
    print("owner is", owner)  # outside a method, variable doesnt need 'self.' or 'classname.' prefix

    def __init__(self, name):  # generic constructor with common name, this init method is overridden in child named Vehicle
        self.name = name  # name is a common variable, so mentioned in parent constructor

    def start(self):  # this is overridden in child with different code
        print(Vehicle.owner+" Vehicle started")  # notice how we give classname.variablename instead of self.varaiblename

    def horn(self, sound):
        print("{} {}, make way".format(sound, sound))  # notice how we don't use self here, directly call sound

    def priv(owner):  # no need of self as we will not call this from object/instance
        print(owner,": check")

class Car(Vehicle):  # child class inheriting from base/parent
    def __init__(self, name, transmission):  # notice how we are overriding the init method of the parent
        super().__init__(name)  # reusing some attributes(like name) definition of init method from parent
        #  super().owner  #we commented this out but this is a class attribute from parent
        self.transmission = transmission  # child attribute, not in parent

    def details(self):  # child method, not in parent
        print("car name is:{} and transmission type is {}".format(self.name, self.transmission))
        print("owner is ", super().owner)

    def start(self):  # class method is overridden
        print("Car started:", self.name)


Audi = Car("Audi", "Automatic")  # creating instance
Audi.details()  # instance method
Audi.start()  # child instance method
Audi.horn("squeak")
#Audi.priv()
Vehicle.start("benz")  # calling parent class method instead, benz is just given as an instance name
Vehicle.horn("benz", "burr")  # benz is the instance name and 'burr' is the sound argument value
Vehicle.priv("venkat")  # calling a private function of the class
# we did method overriding in this example, overriding is when you overwrite method definition in child
