# Let's run a bunch of functions
def square_cube(value):  # simple function to return square and cube
    return value**2, value**3  # returns multiple values


print(square_cube(3))  # function call
# let's see call by value and call by reference situations
small_list = [1, 3, 5, 7, 11]  # we will initialize a list that we can pass as argument
print(small_list)


def appender(s_list):
    s_list.append(15)
    print(s_list)


appender(small_list)  # call function to append value to global list
print(small_list)  # notice how changes in function reflected in global variable
# in the above example the arguments are passed as reference instead of value, as lists are mutable

my_name = "venkat"


def string_mod(new_name):
    new_name = "alt"
    print(new_name)


string_mod(my_name)  # call function to change value
print(my_name)  # changes in function are not reflected in global variable
# since immutable values do not change, there is no need to carry entire object, only value is passed.
# Hence, changes are not reflected
# lists, sets and dictionaries are mutable
# int, float, bool, str, tuple, unicode are immutable.

# parameters can become positional or keyworded when function is called
# not necessarily when function is defined
def parameters(name, age, dept, desig):  #you can assign default values here but make sure non default variables come first
    print("name is {}, age is {}".format(name, age))
    print("department is {}, designation is {}".format(dept, desig))


parameters("Venki", 29, desig='ST Lead', dept='projects')  # this call made first 2 parameters positional and next 2 keyworded
parameters("Venki", 29, 'ST Lead', 'projects')  # this call made all parameters positional
parameters(age=29, desig='ST Lead', dept='projects', name="Venki")  # this call made all parameters keyworded
# keywords should match in function definition and call
