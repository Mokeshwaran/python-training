import functools


def factorial(s):
    if s <= 1:
        return 1
    else:
        return s * factorial(s - 1)


a = [2, 4, 6, 8, 10]
b = [12, 13, 14, 15]
for i in a:
    print(factorial(i))

fact = map(factorial, a)
print(*fact)

factorials = lambda s: 1 if s <= 1 else s * factorials(s - 1)
print(*map(factorials, a))

gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
print(*map(gcd, a, b))

# print(*map(a+b, a, b))

x = {i: j for i, j in enumerate(a, start=20)}
print(x)
x = [(i, j) for i, j in enumerate(a, start=10)]
print(x)


users = [10, 19, 23, 22, 17, 19, 18, 16, 15, 28, 29, 25]

# def is_adult(age):
#     if age >= 18:
#         return True  # Alternatively we can use 1 and 0 replacing True and False respectively.
#     else:
#         return False


age = [x for x in filter(lambda age: True if age >= 18 else False, users)]
print(list(age))


players = zip(a, b)
print(list(players))

print(functools.reduce(lambda a, b: a - b, users))
