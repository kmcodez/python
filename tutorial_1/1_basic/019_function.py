# function = a block of code which is executed only when it is called

def hello(first_name, last_name, age):
    print("hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")
    print("have a nice day!")


# hello("Bro", "Code", 21)


def hello1(name: str):
    print("hello! " + name)
    print("have a nice day!")


# hello1("wtk")


# return statement =  Functions send Python values/objects back to the caller.
#                     These values/objects are known as the function's return value

def multiply(number1, number2):
    return number1 * number2


x = multiply(6, 8)
# print(x)


# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments does not matter, unlike positional arguments
#                     Python knows the names of the argumetns that our function receives.


def hello_2(first: str, middle: str, last: str):
    print(first, middle, last)


# call the function through passing the keyword
hello_2(last="Code", middle="Dude", first="Bro")
