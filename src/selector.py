from math import isnan
from src import generator, randomizer


def menu():
    number_of_words = input("Introduce number of words for password: ")
    joiner = input("Introduce a joiner (or leave a space, or blank for no joiner): ")

    if isnan(int(number_of_words)):
        raise TypeError("Introduce a valid number")
    else:
        password_initial = generator.create_password_from_given_length(int(number_of_words), joiner)

    cap_done = 0
    while cap_done == 0:
        capitalized = input("Do you want it capitalized? (Y/N): ")

        if capitalized == 'Y':
            password_capitalized = randomizer.randomize_upper_case_in_password(password_initial)
            cap_done = 1
            return print("Your new password is: " + password_capitalized)

        elif capitalized == 'y':
            password_capitalized = randomizer.randomize_upper_case_in_password(password_initial)
            cap_done = 1
            return print("Your new password is: " + password_capitalized)

        elif capitalized == 'N':
            cap_done = 1
            return print("Your new password is: " + password_initial)

        elif capitalized == 'n':
            cap_done = 1
            return print("Your new password is: " + password_initial)

        else:
            cap_done = 0
            return print("Error! Please select a correct option (Y/N).")

    ent_done = 0
    while ent_done == 0:
        entropy = input("Do you want to know the entropy? (Y/N): ")

        if entropy == 'Y':
            ent_done = 1
            pass

        elif entropy == 'y':
            ent_done = 1
            pass

        elif entropy == 'N':
            ent_done = 1
            pass

        elif entropy == 'n':
            ent_done = 1
            pass

        else:
            ent_done = 0
            return print("Error! Please select a correct option (Y/N).")
