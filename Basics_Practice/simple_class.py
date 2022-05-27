class Placeholder:  # creating a simple class without any functionality
    pass


place_instance = Placeholder()  # insta nce created
print(place_instance)  # will be printed as object instead of class
print(place_instance.__dict__)  # initially doesn't have any constructor values for instance
place_instance.name = 'venki'  # instance attribute created at runtime
print(place_instance.__dict__)  # now we have instance attribute
class_reference = Placeholder  # direct reference to the class itself, not instance
print(class_reference)  # notice how this is mentioned as class instead of object
print(class_reference.name)  # this should throw error as class doesn't have this attribute
print(class_reference.__dict__)  # shows class attributes
