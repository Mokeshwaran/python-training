from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def details(self):
        return f"{self.name}, {self.age}, In Student"


class Education(Student):
    # If inherited class inherits from a class that contains an
    # abstract method then it must implement that method in inherited class.
    # TypeError: Can't instantiate abstract class Education with abstract method details
    # def details(self):
    ...


class Address(Student):
    def details(self):
        return f"{self.name}, {self.age}, In Address"


a = Address("Mokeshwaran", 23)
print(a.details())
b = Education("Mokeshwaran", 23)
print(b.details())
