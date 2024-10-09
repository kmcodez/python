class Car:

    color = None


class Motorcycle:

    color = None


def change_color(car_intance, color):
    car_intance.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()
bike_2 = Motorcycle()
bike_3 = Motorcycle()

change_color(car_1, "red")
change_color(car_2, "blue")
change_color(car_3, "green")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)
