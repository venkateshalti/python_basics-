# simple python program to demonstrate the usage of private and protected variables
class Isolated:
    color = 'red'
    _taste = 'sour'
    __texture = 'thick'
    print(color, _taste, __texture)  # don't need self here
    def __init__(self, name):
        self.name = name

    def details(self):
        print(self.color)  # class variables must be called as instance variables(self) inside a method
        print(self._taste)
        print(self.__texture)  # this is accessible only because it is in the same class where it's defined
        print(self.name)


grape = Isolated('grapejuice')
grape.details()
print(grape.color)
print(grape._taste)  # this is accessible as single _ is a convention, not a rule
#print(grape.__texture)  #notice how this is not accessible outside the class
print("class attributes")
print(Isolated.color)  # no need to define init values in class call as its not an instance
print(Isolated._taste)  # this is accessible as single _ is a convention, not a rule
#print(Isolated.__texture)  #notice how this is not accessible outside the class