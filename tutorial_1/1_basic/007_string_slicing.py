# slicing = creating a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Bro Code"

# way 1
first_name = name[0:3]
first_name = name[:3]   # above are same
last_name = name[4:]    # name[4:8]
funky_name = name[0:8:3]
new_name = name[::3]     # above are same
reversed_name = name[::-1]


print(first_name)
print(last_name)
print(funky_name)
print(new_name)
print(reversed_name)


# way 2
website1 = "http://google.com"
website2 = "http://wikipedia.com"
# the negative index gets the position from the end.
slice = slice(7, -4)
print(website1[slice])
print(website2[slice])
