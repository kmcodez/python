# lambda function = function written in 1 line using lambda word
#                   accepts any number of arguments, but only has one expression
#                   (think it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
# lambda parameters:expression


# # case 1
# def double(x):
#     return x * 2


# print(double(10))


# # case 2
# if you have learned js, it looks like Arrow function expressions double = x => x * 2
double = lambda x: x * 2
print(double(5))

multiply = lambda x, y: x * y
print(multiply(3, 4))

add = lambda x, y, z: x + y + z
print(add(1, 2, 3))

check_age = lambda age: True if age >= 18 else False
print(check_age(3))

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Bro", "Code"))
