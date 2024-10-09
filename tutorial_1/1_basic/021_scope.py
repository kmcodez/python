# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created


# python used LEGB rule for following
# Local, Enclosing, Global, Built-in

name = "Bro"    # global scope (available anywhere in the code)


def display_name():
    name = "Code"   # local scope (available only inside the function)
    print(name)


display_name()
print(name)
