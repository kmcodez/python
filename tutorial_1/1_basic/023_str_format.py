# str.format() =    optional method that gives users
#                   more control when displaying outputs


animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)

# using the .format() method
print("The {} jump over the {}".format("cow", "moon"))
print("The {} jump over the {}".format(animal, item))

# positional argument
print("The {1} jumped over the {0}".format("cow", "moon"))
print("The {0} jumped over the {1}".format("cow", "moon"))

# keyword argument
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))

text = "The {} jumped over the {}"
print(text.format(animal, item))


name = "Bro"

print("Hello, my name is {}".format(name))

# add padding to a value
print("Hello, my name is {0:10}. Nice to meet you".format(name))

# align your value
print("Hello, my name is {:<10}. Nice to meet you".format(name))  # left alligned
print("Hello, my name is {:>10}. Nice to meet you".format(name))  # right alligned
print("Hello, my name is {:^10}. Nice to meet you".format(name))  # center alligned

# align your value with keyword argument
print("Hello, my name is {name:<10}. Nice to meet you".format(name=name))  # left alligned
print("Hello, my name is {name:>10}. Nice to meet you".format(name=name))  # right alligned
print("Hello, my name is {name:^10}. Nice to meet you".format(name=name))  # center alligned

# format some numbers
number1 = 3.1415926
number2 = 1000

# use two decimal places
print("The number pi is {number:.2f}".format(number=number1))

# insert a comma to the number
print("The number is {:,}".format(number2))

# display your number as binary
print("The number is {:b}".format(number2))

# display your number as octal number
print("The number is {:o}".format(number2))

# display your number as hexadecimal number
print("The number is {:x}".format(number2))
print("The number is {:X}".format(number2))

# display the number in scientific notation
print("The number is {:e}".format(number2))
print("The number is {:E}".format(number2))
