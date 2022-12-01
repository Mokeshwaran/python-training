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
from datetime import date


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
# class Operation(object):
#     def add(self, *args):
#         w = 0
#         for i in args:
#             w += i
#         return w
#
#     def sub(self, *args):
#         w = 0
#         for i in args:
#             w -= i
#         return w
#
#     def mul(self, *args):
#         w = 1
#         for i in args:
#             w *= i
#         return w
#
#     def div(self, a, b):
#         if b == 0:
#             return "Can't divide by 0"
#         return a / b
#
#
# add = Operation().add(1, 2, 3, 4)
# sub = Operation().sub(1, 2, 3, 4)
# mul = Operation().mul(1, 2, 3, 4)
# div = Operation().div(10, 2)
#
# print(add, sub, mul, div)

# class Details:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email
#
#     def __str__(self):
#         return f"{self.name}, {self.age}, {self.email}"
#
#     def delete_details(self):
#         del self.name, self.age, self.email
#
#
# person = Details("Moki", 23, "moki@moki.com")
# print(person.__dict__)
# person.delete_details()
# person_1 = Details("Loki", 26, "loki@loki.com")
# print(person_1.__dict__)
# person_1.delete_details()
# print(person_1.__dict__)
# print(person.__dict__)

class Books:
    title = "Python"

    @classmethod
    def purchase(cls):
        return f"Book Purchased: {cls.title}"


print(Books.purchase())


class Medicine:
    med_manufacturer = "Some Medi Company"

    def __init__(self, title, expiry_date):
        self.title = title
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{self.title}, {self.expiry_date}"

    @staticmethod
    def is_expired(expiry_date):
        return date.today().year - expiry_date > 0

    @classmethod
    def manufacturer(cls):
        return f"{cls.med_manufacturer}"


title = "Paracetemol"
expiry_date = 2021
med = Medicine(title, expiry_date)
print(med)
print(med.is_expired(expiry_date))
print(med.manufacturer())
