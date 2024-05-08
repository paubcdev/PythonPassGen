from math import isnan
from src import generator, capitalizer


def capitalizer_menu(password):
    print("Select capitalizer method: ")
    print("1 - Randomly capitalized.")
    print("2 - All caps.")
    cap_mode = input()
    print(capitalizer.capitalizer(password, cap_mode))


def menu():
    number_of_words = input("Introduce number of words for password: ")
    joiner = input("Introduce a joiner from this set: ( !@#$%^&*_-=+?.,~;: ) (or leave a space): ")

    if isnan(int(number_of_words)):
        raise TypeError("Introduce a valid number")
    else:
        password_initial = generator.create_password_from_given_length(int(number_of_words), joiner)

    checker = 0
    while checker == 0:
        capitalized = input("Do you want it capitalized? (Y/N): ")
        if capitalized == 'y':
            capitalizer_menu(password_initial)
            checker = 1
        elif capitalized == 'Y':
            capitalizer_menu(password_initial)
            checker = 1
        elif capitalized == 'n':
            print(password_initial)
            checker = 1
        elif capitalized == 'N':
            print(password_initial)
            checker = 1
        else:
            print("Please select Y/N!")
            checker = 0

    '''ent_done = 0
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
'''