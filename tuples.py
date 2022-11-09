some_tuple = (
    5, 3, 8,
    1, 6, 7,
    2, 9, 4
)  # Tuple of numbers


def freq_of_elements(tuples, number_to_search):
    # This method will count take the number to search
    # and returns the number of elements in tuples.
    count = 0
    for i in tuples:
        if i == number_to_search:
            count += 1
    return count


flag = True
while flag:  # This while loop is initially set to True, to mimic do-while loop.
    try:
        number = int(input("Enter number to search: "))
        print("Frequency of", number, "is", freq_of_elements(some_tuple, number))
        flag = False
    except ValueError:
        print("Value must be a number")
