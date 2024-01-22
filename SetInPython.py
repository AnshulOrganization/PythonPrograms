"""
Unordered collection of elements
each value is unique
It is mutable
It is enclosed in {}
"""

s = {1, 2, "Anshul"}
print(s, type(s))

# empty set
s1 = set()
# s1 = {}  This will be a dictionary not a set

# If you try to make a set with same elements, Python will drop the Identical values

# Built-in Functions
# add()  adds element to set
s1.add("Anshul")
s1.add("Kumbhare")
s1.add(1)

# length
print(len(s1))

# clear() removes all elements from set
# s1.clear()

# discard() remove the specified item
s1.discard(1)

# pop()  remove an element from set
s1.pop()

# remove()
# s1.remove("Anshul")

# s1.update()
s1.update((1, 2, 3, 4))

# intersection() and union()
a = (1,2,3,4,5,6)
b = (2,5,6,4)


print(s1)