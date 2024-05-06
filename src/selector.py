from math import isnan
from src import generator, capitalizer


def menu():
    number_of_words = input("Introduce number of words for password: ")
    joiner = input("Introduce a joiner from this set: ( !@#$%^&*_-=+?.,~;: ) (or leave a space): ")

    if isnan(int(number_of_words)):
        raise TypeError("Introduce a valid number")
    else:
        password_initial = generator.create_password_from_given_length(int(number_of_words), joiner)

    capitalizer.random_capitalizer(password_initial)

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