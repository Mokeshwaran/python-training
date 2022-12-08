class Celsius(object):
    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

    def __delete__(self, instance):
        print("Deleted...")
        del self.value


class Temperature(object):
    celsius = Celsius()


temp = Temperature()
print(temp.celsius)

temp.celsius = 10
print(temp.celsius)

del temp.celsius
# print(temp.celsius)




# Using __del__ will raise:
# AttributeError: __delete__
# Exception ignored in: <function Celsius.__del__ at 0x000001EE84F6A0C0>
# TypeError: Celsius.__del__() missing 1 required positional argument: 'instance'
