class Automobile:
    """
    This class contains the description of the automobiles.
    """
    def __init__(self, name, wheel_type):
        self.name = name
        self.wheel_type = wheel_type

    def description(self):
        """
        This method returns the description of the Automobile.

        :return: Description of an automobile.
        """
        return f"{self.name}, {self.wheel_type}, Not an automobile"

    def __del__(self):
        print("Destroyed Automobile")


class Car(Automobile):
    def description(self):
        """
        This method returns the description of Car.

        :return: Description of an car.
        """
        return f"This is a car, Name: {self.name}, Wheel Type: {self.wheel_type}"

    def __del__(self):
        print("Destroyed Car.")


class Motorbike(Automobile):
    def description(self):
        """
        This method returns the description of Motorbike.

        :return: Description of a motorbike.
        """
        return f"This is a bike, Name: {self.name}, Wheel Type: {self.wheel_type}"


class Human(Automobile):
    pass


car = Car("Toyota", "4-Wheeler")
motorbike = Motorbike("Yamaha", "2-Wheeler")
human = Human("Mokeshwaran", "2-Legs")
print(car.description())
print(motorbike.description())
print(human.description())
