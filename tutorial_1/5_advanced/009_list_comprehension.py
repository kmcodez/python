# list comprehension = a way to create a new list with less syntax
#                       can mimic lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if /else  for item in iterable]


# case 1
# squares = []
# for i in range(1, 11):
#     squares.append(i * i)
# print(squares)

# # do the same thing as the code above
# squares = list(i * i for i in range(1, 11))  # [expression for item in iterable]
# print(squares)


# case 2
students = [100, 90, 60, 40, 70, 80, 50, 0, 30, 20, 10]
passed_students = list(filter(lambda item: item >= 60, students))  # this is a function filter method
print(passed_students)

passed_students = [i for i in students if i >= 60]  # [expression for item in iterable if conditional]
print(passed_students)

passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)
