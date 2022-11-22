from random import randrange


def generate_number():
    for i in range(1, 10000):
        yield randrange(0, 5)


def users_guess(number, user_guess):
    if next(number) == user_guess:
        return True
    else:
        return False


usr_guess = int(input("Enter a number to guess: "))
is_valid_guess = users_guess(generate_number(), usr_guess)
if is_valid_guess:
    print("Correct")
else:
    print("Incorrect")
