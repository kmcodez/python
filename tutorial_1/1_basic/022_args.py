# *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments


def add(*stuff):
    total = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        total += i
    return total


print(add(1, 2, 5, 6, 7))
