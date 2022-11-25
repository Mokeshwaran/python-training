def some_function(a, b, c=10):
    return a, b, c


print(some_function(1, 2, 3))
print(some_function(1, 2))


# def some_function_part_2(a, b=0, c):  # SyntaxError: non-default argument follows default argument
#     return a, b, c


def some_function_part_3(a=1, b=2, c=3):
    return a, b, c


print(some_function_part_3())
# print(some_function_part_3(c=10, b=20, 13))  # SyntaxError: positional argument follows keyword argument
print(some_function_part_3(c=10, b=20, a=13))


def some_function_part_4(a=10, *args,
                         b=10):  # (*args=10) SyntaxError: var-positional argument cannot have default value
    print(type(args))
    if len(args) == 0:
        return a, b
    else:
        return a, b, args


print(some_function_part_4(1, 3, 5, 7))
print(some_function_part_4(1, 3, 5, 7, 9, 20))
# print(some_function_part_4(a=12, 1, 3, 5, 7, 9, b=20))  # SyntaxError: positional argument follows keyword argument
print(some_function_part_4(1, 3, 5, 7, 9, b=20))
# print(some_function_part_4(a=1, b=3, 5, 7, 9))  # SyntaxError: positional argument follows keyword argument
print(some_function_part_4())


# def some_function_part_5(*val, *args):  # SyntaxError: * argument may appear only once
#     print(type(args))
#     if len(args) == 0:
#         return a
#     else:
#         return args


# def some_function_part_6(**kwargs, **val):  # SyntaxError: arguments cannot follow var-keyword argument
#     return kwargs, val


# def some_function_part_7(*args, **kwargs, *val, **vals):  # SyntaxError: arguments cannot follow var-keyword argument
#     return args, kwargs, val, vals


# def some_function_part_8(**kwargs, a=10, b=20):  # SyntaxError: arguments cannot follow var-keyword argument
#     return kwargs, a, b

def some_function_part_9(**kwargs):
    return kwargs


# some_function_part_9(1, 2, 3, 4)  # TypeError: some_function_part_9() takes 0 positional arguments but 4 were given
print(some_function_part_9(a=1, b=2, c=3))


# def add(a, b, /, c, d, *, e, f, /,):  # SyntaxError: / must be ahead of *
# def add(a, b, *, c, d, *, e, f):  # SyntaxError: * argument may appear only once
def add(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
    return a + b + c + d + e + f


print(add(3, 4, 5, 6, e=7, f=8))
print(add(3, 4, c=1, d=2, e=7, f=8))
print(add(3, 4, 1, d=2, e=7, f=8))

# ---------------------------------------------LAMBDA---------------------------------------------

some_identifier = lambda a: [x for x in a if x % 2 == 0]

print(some_identifier([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# ---------------------------------------------SCOPES---------------------------------------------

def outer():
    a = 10
    def inner():
        nonlocal a
        a = 5
    inner()
    print(a)

outer()

num = 0
# def demo():
#     print(num)  # UnboundLocalError: cannot access local variable 'num' where it is not associated with a value
#     num=1
#     print("The Number is:",num)
# demo()

# ---------------------------------------------BUILT-INS---------------------------------------------

a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50, 60]

x = map(lambda y: y + y[::-1], zip(a, b))
print(list(x))
x = map(lambda a: a, filter(lambda q: q + q if q > 25 else ..., b))
print(list(x))
x = map(lambda y: y + y[::-1], enumerate(a))
print(list(x))
# x = map(lambda y: y + y[::-1], type(a))  # TypeError
# print(list(x))
# x = map(lambda y: y + y[::-1], id(a))  # TypeError
# print(list(x))
x = map(lambda y: y + y, range(10))
print(list(x))