import time

# for loop = a statement that will execute it's block of code
#           a limited amount of times


# method 1
for i in range(10):
    print(i + 1)

# method 2
for i in range(50, 100 + 1, 2):
    print(i)

# method 3
for i in "Bro Code":
    print(i)

# method 4
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print('Happy New Year!')
