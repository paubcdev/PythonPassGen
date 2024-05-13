from math import isnan
from src import generator, capitalizer, entropycalculator


def capitalizer_menu(password):
    print("Select capitalizer method: ")
    print("1 - Randomly capitalized.")
    print("2 - All caps.")
    cap_mode = int(input())
    return capitalizer.capitalizer(password, cap_mode)


def checker(answer):
    check = 0
    while check == 0:
        if answer == 'y':
            check = 1  # 1 for yes
        elif answer == 'Y':
            check = 1
        elif answer == 'n':
            check = 2  # 2 for no
        elif answer == 'N':
            check = 2
        else:
            print("Please select Y/N!")
            check = 0
        return check


def menu():
    number_of_words = input("Introduce number of words for password: ")
    joiner = input("Introduce a joiner from this set: ( !@#$%^&*_-=+?.,~;: ) (or leave a space): ")

    if isnan(int(number_of_words)):
        raise TypeError("Introduce a valid number")
    else:
        password_initial = generator.create_password_from_given_length(int(number_of_words), joiner)

    capitalized = input("Do you want it capitalized? (Y/N): ")
    ans_cap = checker(capitalized)
    if ans_cap == 1:  # 1 for yes
        password_final = capitalizer_menu(password_initial)
        print("Your new password is: " + password_final)
    elif ans_cap == 2:  # 2 for no
        password_final = password_initial
        print(password_final)

    entropy = input("Do you want to know the entropy of it? (Y/N): ")
    ans_ent = checker(entropy)
    if ans_ent == 1:  # 1 for yes
        entropy = entropycalculator.calculator(password_final)
        print("Entropy is: " + str(entropy))
