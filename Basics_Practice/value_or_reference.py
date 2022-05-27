# let's implement call by value and call by reference
# mutable objects(lists, sets, dicts) are call by reference since they have a scope to change
# immutable objects on the other hand don't have a need to change, hence call by value
# let's see how values/references are passed to function
a = [1,2,3]
print("before: ", a)
a.append(4)
print("first append: ", a)
def appender(c):
    c.append(5)
    print(c)
appender(a)
print(a)  # append reflected because reference sent

name = 'venkat'
print(name)
name += "es"
print(name)

def name_append(nam):
    nam += 'h'
    print(nam)
name_append(name)
print(name)  # append didn't reflect because reference sent

# the following code shows call by value/reference for simple assigment statement
# here also mutable is call by reference and immutable is called by value
a = [1,2,3]  # list is mutable
b = a
a.append(4)
print(b)  # called by reference

c = {'a':1, 'b':3}  # dict is mutable
d = c
c['c'] = 5
print(c,d)  # called by reference

e = 'hello'  # string is immutable
f = e
e += ' world'
print(e, f)  # called by value

g = 7  # int is immutable
h = g
g = 8
print(h)  # called by value