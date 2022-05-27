# an iterator is a class which has an iter method to initiate and next method to get next values

class ArrayList:
   def __init__(self, number_list):
       self.numbers = number_list
   def __iter__(self):
       self.pos = 0
       return self
   def __next__(self):
       if(self.pos < len(self.numbers)):
           self.pos += 1
           return self.numbers[self.pos - 1]
       else:
           raise StopIteration
array_obj = ArrayList([1, 2, 3])
it = iter(array_obj)
print(next(it))  # output: 1
print(next(it))  # output: 2
print(next(it))  # output: 3
print(next(it))
# Throws Exception
# Traceback (most recent call last):
# ...
# StopIteration
