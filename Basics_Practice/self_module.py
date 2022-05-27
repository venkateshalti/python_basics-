# let's see how and when to use self
class SelfLess:
    def __init__(not_self, name):  # first position is reserved for any variable that holds instance name
        not_self.name = name

    def selfless_method(self_less):  # notice how we gave a very different variable name from init method variable
        print("instance name is {}".format(self_less.name))  # look how i have given self_less. instead of not_self
        # This is because instance name is stored in new variable name


self_instance = SelfLess('Selfish')
self_instance.selfless_method()
