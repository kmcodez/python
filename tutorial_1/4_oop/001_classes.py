# attributes : is/her  ex. name, age, height

# methods : actions  # ex. walk, run, eat, sleep

from modules.car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("ford", "Mustang", 2022, "red")

# access class variable
print(car_1.wheels)

# update the class variable
car_1.wheels = 2
print(car_1.wheels)
print(car_2.wheels)

# access instance variable
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

# access the class function
car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()
