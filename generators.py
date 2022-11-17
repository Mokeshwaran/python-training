def square_numbers(square_list):
    """
    This method is used for squaring and appending it to the list.
    This method is devoid of a python generator.
    :param square_list: List to square.
    :return: empty_list containing the squared values.
    """
    empty_list = []
    for i in square_list:
        empty_list.append(i**2)
    return empty_list


def cube_numbers(cube_list):
    """
    This method is used for cubing the values and yielding it.
    This method uses python generator. Also yield keyword will return multiple
    values until the end.
    :param cube_list: List to cube.
    :return: yields cubed value
    """
    for i in cube_list:
        yield i**3


a = [1, 2, 3, 4, 5]
print("Square Numbers Without Generator: ", square_numbers(a))
print("Object Of The cube_numbers Generator Method: ", cube_numbers(a))
# Here this will print out the generator object.

for i in cube_numbers(a):
    '''
    This 'for' Loop Is Used To Print The Generated Value Without The Displaying 
    Object As It Is...
    '''
    print(i)

print("List Representation Of The Generator: ", list(cube_numbers(a)))
# Here, this will print out the list of cube numbers.

print("Set Representation Of The Generator: ", set(cube_numbers(a)))
print("Tuple Representation Of The Generator: ", tuple(cube_numbers(a)))
# Also we can do it in other data structure.

key_value = zip(a, cube_numbers(a))
# Using zip() will make a tuple out of the given inputs.
print(dict(key_value))

quad_powered = [x**4 for x in a]
# Here I used list comprehension to simplify the process.
print("List Comprehension: ", quad_powered)

pent_powered = (x**5 for x in a)
# Also you can put parentheses to specify it as a generator.
# The name of the generator function will be <genexpr>
print("Generator Comprehension (Proved By Displaying Generator Object): ", pent_powered)
print("Unpacking The Generator Object Using (*): ", *pent_powered)

hex_powered = (x**6 for x in a)
for i in range(6):
    # Note that I gave range value as 6 even though the max length is 5.
    # The generator will show StopIteration after all the elements are exhausted
    # which means if it reaches the end it will throw StopIteration.
    print("Using next() to get the next value: ", next(hex_powered))
