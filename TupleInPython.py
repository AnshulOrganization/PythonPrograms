"""
Tuple is a collection of dissimilar elements
It is immutable
enclosed in ()
it has positive and negative Indexing
"""

t1 = (1, 2, "a", "5")
t2 = tuple(range(5, 16))
print(t1, type(t1), t2, type(t2))

# empty tuple
t3 = ()
t4 = tuple()
print(t3, t4)

"""
Single element inside a tuple is not considered as tuple but as an integer
        t = (10)        <class 'int'>

Tuple with single element is created as follows:

    t = (10, )
"""

# length
print(len(t2))

# Indexing
print(t2[0])

# slicing
print(t2[0:6:2])

# count()
print(t2.count(6))

# index()
print(t2.index(15))

# del
# del t2
print(t2)