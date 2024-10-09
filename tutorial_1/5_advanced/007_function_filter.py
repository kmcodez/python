# filter() = creates a collection of elements from an iterable for which a function returns True
#
# filter(function, iterable)

friends = [
    ("Rachel", 19), 
    ("Monica", 18),
    ("Phoebe", 17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20),
]

# get the people over the drinking age
age = lambda data: data[1] >= 18
print(list(filter(age, friends)))

names = lambda data_names: data_names[0] == 'Joey'
print(list(filter(names, friends)))
