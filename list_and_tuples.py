# tuples

x = 5,6,7,8,3
x = (5,6,7,8,3)
print(x)

# List
y = [5,6,7,8,3]

# Difference between list and tuple
#
# Literal
# someTuple = (1,2)
# someList  = [1,2]
# Size
#
# a = tuple(range(1000))
# b = list(range(1000))
#
# a.__sizeof__() # 8024
# b.__sizeof__() # 9088
# Due to the smaller size of a tuple operation with it a bit faster but not that much to mention about until you have a huge amount of elements.
# Permitted operations
#
# b    = [1,2]
# b[0] = 3       # [3, 2]
#
# a    = (1,2)
# a[0] = 3       # Error
# that also mean that you can't delete element or sort tuple. At the same time you could add new element to both list and tuple with the only difference that you will change id of the tuple by adding element
# a     = (1,2)
# b     = [1,2]
#
# id(a)          # 140230916716520
# id(b)          # 748527696
#
# a   += (3,)    # (1, 2, 3)
# b   += [3]     # [1, 2, 3]
#
# id(a)          # 140230916878160
# id(b)          # 748527696
# Usage
#
# List being mutable can't be used as a key in the dictionary, while tuple can be used. as key in dictionary.
# a    = (1,2)
# b    = [1,2]
#
# c = {a: 1}     # OK
# c = {b: 1}     # Error