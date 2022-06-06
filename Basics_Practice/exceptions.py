# creating a simple function to demonstrate exceptions

def exception_handling():
    try:
        open("nothing to open")  # giving wrong file path
    except Exception as e:  # e represents an instance of a custom sub-class derived from built-in 'Exception' base class
        if hasattr(e, 'message'):  # sometimes, exceptions dont have an attribute named 'message', this can be checked with hasattr()
            print(e.message)  # if it has message attribute, print that message
        else:
            print(e)  # else directly print the instance
    else:  # only get executed when none of the exceptions mentioned are raised
        print("we didn't get any exception")
    finally:  # this gets executed irrespective of other steps but at end of exception handling
        print("print anyway")  # typically we use this to close opened database connections or end any sessions

exception_handling()

# exceptions are hierarchical in nature
# if you encounter an exception, it can be identified with its parent or child class as well

try:
    f = open('nonexistent_file')  # we get a file not found error which is a subclass of OS
except OSError: # we encounter this step first, so the next more accurate exception is ignored
    print('OS Error')
except FileNotFoundError:
    print('File not found Error')

try:
    f = open('nonexistent_file')
except FileNotFoundError: # this is more accurate exception and also comes first
    print('File not found Error')
except OSError:
    print('OS Error')

# checking else part
try:
    f = open('decorators.py')
except FileNotFoundError: # this is more accurate exception and also comes first
    print('File not found Error')
except OSError:
    print('OS Error')
else:  # didnt get any exceptions, hence executing else part
    print('was able to open file without exceptions')
finally:  # will execute anyway, using this to close open connections and files
    print('closing the file')
    f.close()


# let's raise a custom exception
# we start with defining an exception class inherited from Exception base
class CustomException(Exception):
    # this init is needed only if we are trying to customize exception
    def __init__(self, numerator):
        self.numerator = numerator

    def __str__(self):
        return f'you cant divide {self.numerator} by zero'

# let's define a function that raises an exception when certain condition is met, example -> divide by zero
def divide(a,b):
    if b == 0:
        raise CustomException(a)  # 'raise' keyword raises exception class defined above
    else:
        return a/b

# when someone calls above function with denominator argument zero, they will get the defined exception
try:
    res = divide(3,0)
except CustomException as e:
    print(e)
#giving non-zero deonominator
try:
    res = divide(3,1)
except CustomException as e:
    print(e)
else:
    print(res)