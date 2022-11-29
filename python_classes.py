# # SAMPLE FROM THE WEB TO UNDERSTAND
# class Dog:
#     species = "Canis familiaris"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # Instance method
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
#
#
# miles = Dog("Miles", 4)
# # print(miles.description())
# print(miles)
# print(miles.speak("Hello"))
# print(miles.speak("Woof"))
#

# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
#
#     def __str__(self):
#         return f"The {self.color} car has {self.mileage} miles."
#
#
# blue_car = Car("Blue", 20000)
# print(blue_car)
# red_car = Car("Red", 30000)
# print(red_car)

# MY SAMPLE PROGRAM TO IMPLEMENT CLASSES.
class Operation(object):
    def add(self, *args):
        w = 0
        for i in args:
            w += i
        return w

    def sub(self, *args):
        w = 0
        for i in args:
            w -= i
        return w

    def mul(self, *args):
        w = 1
        for i in args:
            w *= i
        return w

    def div(self, a, b):
        if b == 0:
            return "Can't divide by 0"
        return a / b


add = Operation().add(1, 2, 3, 4)
sub = Operation().sub(1, 2, 3, 4)
mul = Operation().mul(1, 2, 3, 4)
div = Operation().div(10, 2)

print(add, sub, mul, div)
