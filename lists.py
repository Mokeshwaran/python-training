def fibonacci_list(no_of_elements):
    """
    The fibonacci_list will have one parameter and returns a list of fibonacci series.

    :param no_of_elements: Number of elements given by the user.
    """
    fibonacci = []
    number_1 = 0  # Assigning initial values for computational purposes.
    number_2 = 1

    for i in range(0, no_of_elements):
        fibonacci.append(number_1)
        number_3 = number_1 + number_2
        # Sum 2 values and assigning it to a 3rd variable.
        number_1 = number_2
        number_2 = number_3

    return fibonacci


number_of_elements = int(input("Enter number of values: "))
print(fibonacci_list(number_of_elements))
