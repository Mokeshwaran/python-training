# add = lambda a, b: a + b
# sub = lambda a, b: a - b
# operate = lambda func, a, b: func(a, b)
#
# print(operate(sub, 10, 20))
#
import math
#
#
# def is_called():
#     def is_returned():
#         print("Hello")
#     return is_returned
#
#
# new = is_called()
# new()

# def some_func(func):
#     def inner():
#         print("something to print before returning func...")
#         func()
#     return inner
#
#
# @some_func
# def another_func():
#     print("Hello from another_func")
#
# another_func()

# def divide(func):
#     print("Dividing two numbers")
#
#     def inner(a, b):
#         if b == 0:
#             return "Can't divide by 0"
#         return func(a, b)
#
#     return inner
#
#
# @divide
# def deivi(a, b):
#     return a / b
#
#
# print(deivi(10, 2))
# print(deivi.__code__.co_freevars)
# print(deivi.__code__.co_code)
# print(deivi.__code__.co_name)
# print(deivi.__code__.co_flags)
# print(deivi.__code__.co_names)
# print(deivi.__code__.co_argcount)
# print(deivi.__code__.co_cellvars)
# print(deivi.__code__.co_consts)
# print(deivi.__code__.co_filename)
# print(deivi.__code__.co_firstlineno)
# print(deivi.__code__.co_kwonlyargcount)
# print(deivi.__code__.co_linetable)
# print(deivi.__code__.co_lnotab)
# print(deivi.__code__.co_posonlyargcount)
# print(deivi.__code__.co_nlocals)
# print(deivi.__code__.co_stacksize)
# print(deivi.__code__.co_varnames)
# print(deivi.__code__.co_positions())
# print(deivi.__closure__)


def square_root_eqn(func):
    def inner(a, b, c):
        d = b ** 2 - 4 * a * c
        func(a, b, d)

    return inner


def second_part(func):
    def inner(a, b, d):
        q = -b + math.sqrt(d)
        func(a, q)

    return inner


@square_root_eqn
@second_part
def quad(a, quad_eqn):
    return quad_eqn / 2 * a

square_root_eqn(second_part(quad(1, 5 ,6)))
print(quad(1, 5, 6))


def error_message(func):
    def inner(a, b):
        if b == 0:
            return "Error can't divide by 0"
        else:
            return func
    return inner


@error_message
def divide(a, b):
    return a / b


@error_message
def modulo(a, b):
    return a % b


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(divide(a, b))
print(modulo(a, b))
