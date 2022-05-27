
# there are 3 ways of copying -> assignment, shallow copy, deepcopy
# = or assignment creates a new variable but the variable simply refers to existing original object
# 'copy' creates a new object for existing data, however, if it has sub objects, they are still referred from original
# 'deep copy' creates a new object where even sub objects are created entirely instead of reference
# lets understand with a simple example and move to complex example
import copy
simple_list = [1, 2, 3]  # list initialization
a = simple_list  # simple assignment, 'a' will have same values and same object as simple_list
b = copy.copy(simple_list)  # 'b' is created as a new object with references of elements of 'simple_list'
c = copy.deepcopy(simple_list)  # 'c' is created as a new object with and even its elements are new copies
print(simple_list)  # original values
print(id(simple_list))  # original address
print(a)  # original values same as original simple_list
print(id(a))  # original address same as original simple_list
print(b)    # original values same as original simple_list
print(id(b))  # original address NOT same as original simple_list
print(c)    # original values same as original simple_list
print(id(c)) # original address NOT same as original simple_list or 'b'
simple_list.append(6)  # modifying 'a' to confirm dependencies
print(simple_list)  # new values
print(id(simple_list))  # new address same as original simple_list
print(a)  # new values same as new simple_list
print(id(a))  # new address same as original simple_list
print(b)  # new values same as original simple_list
print(id(b))  # new address same as old values of b
print(c)  # new values same as original simple_list
print(id(c))  # new address same as old values of c

#  now, lets apply the same code to compound objects to understand the functionality better
simple_list = [1, 2, [6, 9], 3,]  # compound list initialization
a = simple_list  # simple assignment, 'a' will have same values and same object as simple_list
b = copy.copy(simple_list)  # 'b' is created as a new object with references of elements of 'simple_list'
c = copy.deepcopy(simple_list)  # 'c' is created as a new object with and even its elements are new copies
print(simple_list[2], id(simple_list[2]))
print(a[2], id(a[2]))
print(b[2], id(b[2]))  # same address because this is reference
print(c[2], id(c[2]))  # different address because this is not reference
simple_list[2].append(3)  # modifying 'a' to confirm dependencies
print(simple_list[2], id(simple_list[2]))
print(a[2], id(a[2]))
print(b[2], id(b[2]))  # notice how the values of sub object changed as the sub object changed in simple_list
print(c[2], id(c[2]))  # notice how the values of sub object retained because of true copying