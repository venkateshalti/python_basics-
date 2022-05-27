# just replicating all previous Basics_Practice
def exception_handling():
    try:
        open("nothing to open")  # giving wrong file path
        '''
    except Exception as e:  # storing the raised exception in variable object e
        if hasattr(e, 'message'):  # sometimes, exceptions dont have an attribute named 'message', this can be checked with hasattr()
            print(e.message)  # if it has message attribute, print that message
            return None
        else:
            print(e)  # else directly print the instance
        '''
    except TypeError:
        run_code2()
        return None
    else:  # only get executed when none of the exceptions mentioned are raised
        print("we didn't get any exception")
    finally:  # this gets executed irrespective of other steps but at end of exception handling
        print("print anyway")  # typically we use this to close opened database connections or end any sessions

exception_handling()
print('missing')