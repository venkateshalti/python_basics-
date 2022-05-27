# before writing full-blown decorators, lets start with passing functions as arguments
def add(x):  # inner function addition definition
    return x+1  # return value plus one


def sub(x):  # inner function subtraction definition
    return x-1  # return value minus one


def calc_static(func_choice):  # outer function with hardwired value
    return func_choice(27)  # value 27 is hardwired


print("calling addition function: ", calc_static(add))  # pass add function as parameter to outer function
print("calling subtraction function: ", calc_static(sub))  # pass sub function as parameter to outer function


def calc(func_choice, value):  # outer function along with value are defined as arguments
    return func_choice(value)  # call outer function by passing it a dynamic value


print("calling addition function: ", calc(add, 7))  # pass add function and value 7 as parameters to outer function
print("calling subtraction function: ", calc(sub, 11))  # pass sub function and value 11 as parameters to outer function

# so far we have passed functions as arguments to other functions at same level
# now, lets decorate functions around each other, this is without arguments for now
def decorator_function(funct):  # decorated function has been passed as argument
    def say_hello():  # local function that wraps around the decorated function
        print("before calling")
        funct()  # calling the decorated function
        print("after calling")
    return say_hello  # notice that we didn't use parenthesis () as we are returning function code, instead of executing
    # say_hello is returned as a whole, just like how we pass function as argument, say_hello is NOT executed

@decorator_function  # wrapper function
def decorated_function():
    print("inside wrapped")


decorated_function()  # calling a function that has been decorated

# let's define some decorators with arguments
def smart_divide(func):
    def inner(c, d):# notice how we used c,d instead of a,b and still same values passed
        print("I am going to divide", c, "and", d)
        if d == 0:
            print("Whoops! cannot divide")
            return  # this will end the program without calling decorated function

        return func(c, d)  # calling decorated function
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(2,5)  # function call with valid data
divide(2,0)  # function call with invalid data

# we can see nesting of decorators below
def star(func):  # simple function one
    def inner(*args, **kwargs):  # call positional parameters first followed by keyword parameters
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):  # simple function two
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star  # topmost decorator will wrap at last
@percent  # bottommost decorator will wrap at first
def printer(msg):
    print(msg)  # this will go into percent first and get embedded there
    # the whole part inside inner including the function call will be returned
    # the whole part returned above will be sent to star and get wrapped and returned one more time for execution


printer("Hello")