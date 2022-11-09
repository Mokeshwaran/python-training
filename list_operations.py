def add(name):
    """
    This method will add an element to the list.

    :param name: Name given by the user.
    :return: list of names.
    """
    names.append(name)
    return names


def delete(name):
    """
    This method will delete an element from the list.

    :param name: Name given by the user.
    :return: list of names.
    """
    names.remove(name)
    return names


def view():
    """
    This method will display the list of elements.

    :return: list of names.
    """
    return names


names = []  # Empty list to add names
flag = True
while flag:  # This while loop is initially set to True, to mimic do-while loop.
    choice = int(input('Choose 1: '))
    if choice == 1:
        add(input('Enter a Name to add: '))  # Adds a name
        flag = True

    elif choice == 2:
        try:
            delete(input('Enter a Name to delete: '))  # Deletes a name
            flag = True
        except ValueError:
            print('Entered value doesn\'t exist')  # Thrown if the data is not found.

    elif choice == 3:
        print(view())  # Display names
        flag = True

    else:
        flag = False  # Making flag false to break the loop.
        pass
