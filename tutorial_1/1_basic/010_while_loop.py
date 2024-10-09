# while loop = a statement that will execute it's block of code
#               as long as it's condition remains true

# method 1
name = ""
while len(name) == 0:
    name = input("Enter your name: ")

# method 2
name = None
while not name:
    name = input("Enter your name: ")

print("Hello " + name)


# method 3
while True:
    print("Help! I am stcuck in the loop")
