# sort() method     = used with lists
# sorted() function   = used with iterable


# case 1
students = ["Squidward", "Sandy", "Patrick", "Spongbb", "Mr.Krabs"]

# only for the list using sort
students.sort()
students.sort(reverse=True)
print(students)


studentss = ("Squidward", "Sandy", "Patrick", "Spongbb", "Mr.Krabs")
# used with iterable
sorted_student = sorted(students)
sorted_student = sorted(students, reverse=True)
print(sorted_student)


# case 2
students = [
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongbb", "B", 20),
    ("Mr.Krabs", "C", 78),
]

students.sort()
students.sort(reverse=True)

name = lambda names: names[0]  # when sorting names
students.sort(key=name)
students.sort(key=name, reverse=True)

section = lambda sections: sections[1]
students.sort(key=section)
students.sort(key=section, reverse=True)

age = lambda ages: ages[2]
students.sort(key=age)
students.sort(key=age, reverse=True)


# case 3
students = (
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongbb", "B", 20),
    ("Mr.Krabs", "C", 78),
)

sorted_student = sorted(students)
sorted_student = sorted(students, reverse=True)

name = lambda names: names[0]
sorted_student = sorted(students, key=name)
sorted_student = sorted(students, key=name, reverse=True)

section = lambda sections: sections[1]
sorted_student = sorted(students, key=section)
sorted_student = sorted(students, key=section, reverse=True)

age = lambda ages: ages[2]
sorted_student = sorted(students, key=age)
sorted_student = sorted(students, key=age, reverse=True)


for i in sorted_student:
    print(i)
