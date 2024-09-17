T"""
Python Dictionary is a collection of Key:Value pairs

TESTING FOR PULL REQUEST API

Keys are unique
Value can be duplicated
"""

d = {
    1: "Anshul",
    2: "Omkar",
    3: "Abijith"
}

print(d, len(d), type(d), sep="\n")

d1 = dict(
    (('a', 97), ('b', 98))
)

print(d1, len(d1), type(d1), sep="\n")

# empty dictionary
d2 = {}
d3 = dict()
print(type(d2), type(d3))

# accessing key and value pairs
print(d[2])
print(d[3])
print(d1['a'])

# Adding values in dictionary
d[1] = "Sandeep"
print(d)

d[99] = "Saurabh"
print(d)

# get()
print(d.get(99))

# clear()           removes all elements from dictionary

# get()             returns the value of specified key

# items()           returns a list containing a tuple for each key value pair
print(d.items())

# keys()            returns list containing keys
print(d.keys())

# values()          returns a list containing values
print(d.values())

# pop()             removes element with a specified key
# popitem()         removes last inserted key value pairs

# update()          updates the dictionary with specified key value pairs
