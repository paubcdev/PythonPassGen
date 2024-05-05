from math import isnan
from src import generator, randomizer


def menu():
    number_of_words = input("Introduce number of words for password: ")
    joiner = input("Introduce a joiner (or leave a space, or blank for no joiner): ")

    if isnan(int(number_of_words)):
        raise TypeError("Introduce a valid number")
    else:
        password_initial = generator.create_password_from_given_length(int(number_of_words), joiner)

    done = 0
    while done == 0:
        capitalized = input("Do you want it capitalized? Please select Y/N: ")

        if capitalized == 'Y':
            password_capitalized = randomizer.randomize_upper_case_in_password(password_initial)
            done = 1
            return print("Your new password is: " + password_capitalized)

        elif capitalized == 'y':
            password_capitalized = randomizer.randomize_upper_case_in_password(password_initial)
            done = 1
            return print("Your new password is: " + password_capitalized)

        elif capitalized == 'N':
            done = 1
            return print("Your new password is: " + password_initial)

        elif capitalized == 'n':
            done = 1
            return print("Your new password is: " + password_initial)

        else:
            done = 0
            return print("Error! Please select a correct option.")

