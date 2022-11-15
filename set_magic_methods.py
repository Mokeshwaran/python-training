def and_operation(first, second):
    """
    This method will do the AND operation.

    :param first: Set given by the user
    :param second: Set given by the user
    :return: None
    """
    print("AND Operation: ", first.__and__(second))
    print("In-place AND Operation: ", first.__iand__(second))
    print("Reverse AND Operation", first.__rand__(second))


def xor_operation(first, second):
    """
    This method will do the XOR operation.

    :param first: Set given by the user
    :param second: Set given by the user
    :return: None
    """
    print("XOR Operation: ", first.__xor__(second))
    print("In-place XOR Operation: ", first.__ixor__(second))
    print("Reverse XOR Operation: ", first.__rxor__(second))


def or_operation(first, second):
    """
    This method will do the OR operation.

    :param first: Set given by the user
    :param second: Set given by the user
    :return: None
    """
    print("OR Operation: ", first.__or__(second))
    print("In-place OR Operation: ", first.__ior__(second))
    print("Reverse OR Operation: ", first.__ror__(second))


def sub_operation(first, second):
    """
    This method will do the Subtraction operation.

    :param first: Set given by the user
    :param second: Set given by the user
    :return: None
    """
    print("Subtraction Operation: ", first.__sub__(second))
    print("In-place Subtraction Operation: ", first.__isub__(second))
    print("Reverse Subtraction Operation: ", first.__rsub__(second))


def not_equal(first, second):
    """
    This method will do the Not Equal operation.

    :param first: Set given by the user
    :param second: Set given by the user
    :return: None
    """
    print("Not Equal Operation: ", first.__ne__(second))


def equal(first, second):
    """
    This method will do the Equal operation.

    :param first: Set given by the user
    :param second: Set given by the user
    :return: None
    """
    print("Equal Operation: ", first.__eq__(second))


def greater_than_equal(first, second):
    """
    This method will do the Greater Than or Equal operation.

    :param first: Set given by the user
    :param second: Set given by the user
    :return: None
    """
    print("Greater Than Equal Operation: ", first.__ge__(second))


def lesser_than_equal(first, second):
    """
    This method will do the Lesser Than or Equal operation.

    :param first: Set given by the user
    :param second: Set given by the user
    :return: None
    """
    print("Lesser Than Equal Operation: ", first.__le__(second))


def greater_than(first, second):
    """
    This method will do the Greater Than operation.

    :param first: Set given by the user
    :param second: Set given by the user
    :return: None
    """
    print("Greater Than Operation: ", first.__gt__(second))


def lesser_than(first, second):
    """
    This method will do the Lesser Than operation.

    :param first: Set given by the user
    :param second: Set given by the user
    :return: None
    """
    print("Lesser Than Operation: ", first.__lt__(second))


def length_operation(first):
    """
    This method will get the length of the given set.

    :param first: Set given by the user
    :return: None
    """
    print("Length Operation", first.__len__())


def repr_operation(first):
    """
    This method will represent the given set as an object.

    :param first: Set given by the user
    :return: None
    """
    print("Representation Operation: ", first.__repr__())


def str_operation(first):
    """
    This method will represent the given set as a string.

    :param first: Set given by the user
    :return: None
    """
    print("String Operation: ", first.__str__())


def sizeof_set(first):
    """
    This method will get the memory size of the given set.

    :param first: Set given by the user
    :return: None
    """
    print("Size Of Operation: ", first.__sizeof__())


def contains_element(first):
    """
    This method will notify if the entered element is available or not in a set.

    :param first: Set given by the user
    :return: None
    """
    element = input("Enter the element to find: ")
    print("Contains Operation: ", first.__contains__(element))


flag = True
while flag:  # This while loop is initially set to True, to mimic do-while loop.
    primary = set(input("Enter the first set: "))
    secondary = set(input("Enter the second set: "))
    print('1. OR Operations\n'
          '2. AND Operations\n'
          '3. XOR Operations\n'
          '4. Sub Operation\n'
          '5. Not Equal Operation\n'
          '6. Equal Operation\n'
          '7. Lesser Than Operation\n'
          '8. Lesser Than Equal Operation\n'
          '9. Greater Than\n'
          '10. Greater Than Equal\n'
          '11. Length Operation\n'
          '12. Size Of Operation\n'
          '13. Repr Operation\n'
          '14. Str Operation\n'
          '15. Contains Operation')
    choice = int(input("Enter the choice: "))
    if choice == 1:
        or_operation(primary, secondary)

    if choice == 2:
        and_operation(primary, secondary)

    if choice == 3:
        xor_operation(primary, secondary)

    if choice == 4:
        sub_operation(primary, secondary)

    if choice == 5:
        not_equal(primary, secondary)

    if choice == 6:
        equal(primary, secondary)

    if choice == 7:
        lesser_than(primary, secondary)

    if choice == 8:
        lesser_than_equal(primary, secondary)

    if choice == 9:
        greater_than(primary, secondary)

    if choice == 10:
        greater_than_equal(primary, secondary)

    if choice == 11:
        length_operation(primary)

    if choice == 12:
        sizeof_set(primary)

    if choice == 13:
        repr_operation(primary)

    if choice == 14:
        str_operation(primary)

    if choice == 15:
        contains_element(primary)

    else:
        flag = False
