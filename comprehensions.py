def generate_square_numbers():
    """
    This method will generate square numbers till 5
    :return: empty_list with squared values
    """
    empty_list = []
    for i in range(5):
        empty_list.append(i * i)
    return empty_list


def list_comprehension(a):
    """
    This method uses list comprehension to filter the values.
    :param a: list of squared numbers
    :return: filtered list of squared numbers
    """
    return [i for i in a if i % 2 == 0]


set_comprehension = {i for i in list_comprehension(generate_square_numbers())}

dict_comprehension = {x+10: x ** 2 for x in set_comprehension}

print("Generated Square Numbers: ", generate_square_numbers())
print("List Comprehension: ", list_comprehension(generate_square_numbers()))
print("Set Comprehension: ", set_comprehension)
print("Dictionary Comprehension: ", dict_comprehension)

nested_comprehension = [[i for i in set_comprehension]
                        for x in dict_comprehension]
print("\nNested Comprehension: ", nested_comprehension)

chained_comprehension = [i for i in set_comprehension
                         for j in dict_comprehension
                         for x in list_comprehension(generate_square_numbers())]
# The above both comprehensions works like a for loop, like this,
# a = []
# for i in set_comprehension:
#     for j in dict_comprehension:
#         for x in list_comprehension(generate_square_numbers()):
#             a.append(i)
print("\nChained Comprehension: ", chained_comprehension)
