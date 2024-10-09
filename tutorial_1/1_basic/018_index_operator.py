# index operator [] = give access to a sequence's elements (set, list, tuple)
#                       by their position in the sequence

name = "bro Code!"

if name[0].islower():
    name = name.capitalize()

print(name)

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)
