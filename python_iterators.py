# for loop is implemented as follows

a = iter("asdfgh")

while True:
    try:
        print(next(a))
    except StopIteration:
        break


# Custom iterator
class Exponent:
    def __init__(self, max_value=0):
        self.max_value = max_value

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        if self.number <= self.max_value:
            result = 2 ** self.number
            self.number += 1
            return result
        else:
            raise StopIteration


b = Exponent(5)
i = iter(b)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
