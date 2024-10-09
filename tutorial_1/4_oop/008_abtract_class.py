# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract methods = a method has a declaration but does not have an implementation.

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the Car")

    def stop(self):
        print("The car is stopped")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("The motorcycle is stopped")


car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()
car.stop()
motorcycle.stop()
