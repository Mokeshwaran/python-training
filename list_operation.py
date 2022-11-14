def add_names():
    """
    This method will add names to the list.

    :return: List of names after adding
    """
    number_of_values = int(input("Enter the number of value to add: "))
    for index in range(number_of_values):
        values = input("Enter the values: ")
        names.append(values)
    return names


def view_all():
    """
    This method will display all the names from the list.

    :return: List of names
    """
    return names


def filter_names():
    """
    This names will filter names based on the words given by the user.

    :return: Filtered list of names
    """
    filter_word = input("Type the name to filter: ")
    filtered_names = []
    for index in names:
        if index.startswith(filter_word):
            # If the name starts with filter_word,
            # then that name will be appended with the filtered_names.
            filtered_names.append(index)
    return filtered_names


def delete_name():
    """
    This method will delete a name given by the user.

    :return: List of names after deletion
    """
    name = input("Enter the name to remove: ")
    for index in names:
        if index == name:
            names.remove(name)
    return names


def remove_last_name():
    """
    This method will remove the last element from the list.

    :return: List of names after removing the last element
    """
    names.pop()
    return names


def reverse_names():
    """
    This method will reverse all the elements in the list.

    :return: List of names of reversing
    """
    names.reverse()
    return names


def sort_names_a_z():
    """
    This method will sort the names alphabetically.

    :return: List of names after ordering alphabetically.
    """
    names.sort()
    return names


def sort_names_z_a():
    """
    This method will sort the names reverse alphabetically.

    :return: List of names after ordering reverse alphabetically.
    """
    names.sort()
    names.reverse()
    return names


def count_names(name):
    """
    This method will count the number of given name in the list.

    :param name: Name given by the user
    :return: Count of the given name
    """
    return names.count(name)


names = []  # This list is defined globally because of losing data while operating.
flag = True
while flag:  # While loop initially set to True to mimic do-while loop.
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(add_names())
    elif choice == 2:
        print(view_all())
    elif choice == 3:
        print(filter_names())
    elif choice == 4:
        print(delete_name())
    elif choice == 5:
        print(remove_last_name())
    elif choice == 6:
        print(sort_names_a_z())
    elif choice == 7:
        print(sort_names_z_a())
    elif choice == 8:
        print(count_names(input("Enter the name to count the number of names: ")))
    else:
        flag = False
