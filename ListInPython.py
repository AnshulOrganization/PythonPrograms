"""
List is collection of elements of dissimilar datatypes
it is mutable
It has positive and Negative indexing
Elements are closed in []
"""

l1 = [1, 2, 3.0, "Arjun", 5]
print(l1, type(l1))
print(len(l1))

l2 = list("1234gdd")
print(l2, type(l2))
print(len(l2))   # length

# empty list
l3 = []
l4 = list()
print(l3, l4)

# accessing elements
print(l1[0])
print(l1[-1])

# slicing
print(l1[1:4:1])

# change value at index
l1[3] = "Anshul"
print(l1)

# membership Operators
a = [1, 2, 3, 4, 5, 6, 7, 1, 1, 1]
print(2 in a)
print(8 in a)

# Concatenation

a1 = ['a', 'b', 1, 2, 4, 5]
b1 = [1.0, 2.0, 3.5]

print(a1 + b1)

# Asterisk *
a2 = [1, 2, 3] * 3
print(a2)

# Comparison Operators only works when both list have same Datatypes
# (==, >=, >, <, <=, !=)

# List Comprehension (It is a shorthand Syntax)
l = [1, 2, 3, 4, 5, 6]
e_l = [i for i in l if i % 2 == 0]
o_l = [i for i in l if i % 2 != 0]
print(e_l, o_l, sep="\n")


# built in methods( len(), count(), index(), append(), insert(), pop(), del, remove(), sum(), max(), min() )
list1 = [10, 20, 30]

print(len(list1))
print(list1.count(10))

print(list1.index(20))  # shows the index of the value entered

list1.append("Anshul")  # Adds item at the end
print(list1)

list1.insert(1, "Hello")   # insert element at particular index
print(list1)

list1.pop(2)
print(list1)

del l1
# print(l1)

list1.remove("Hello")
print(list1)

list2 = [10, 20, 30]
print(sum(list2), min(list2), max(list2))
