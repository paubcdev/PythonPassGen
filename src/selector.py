from math import isnan
from src import generator, capitalizer, entropycalculator, hashing


def capitalizer_menu(password):
    print("Select capitalizer method: ")
    print("1 - Randomly capitalized.")
    print("2 - All caps.")
    cap_mode = int(input())
    return capitalizer.capitalizer(password, cap_mode)


def hashing_menu(password):
    print("Select hashing method: ")
    print("1- SHA2-256")
    print("2- SHA3-256")
    print("3- BLAKE2b")
    hash_mode = int(input())
    return hashing.hasher(password, hash_mode)


def checker(type_of_checker):
    check = 0
    while check == 0:
        answer = ""

        match type_of_checker:
            case "capitalized":
                answer = input("Do you want it capitalized? (Y/N): ")
            case "entropy":
                answer = input("Do you want to know the entropy? (Y/N): ")
            case "hashing":
                answer = input("Do you want it hashed? (Y/N): ")

        match answer:
            case 'y':
                check = 1  # 1 for yes
            case 'Y':
                check = 1
            case 'n':
                check = 2  # 2 for no
            case 'N':
                check = 2
            case _:
                print("Please select Y/N!")
                check = 0
    return check


def menu():
    number_of_words = input("Introduce number of words for password: ")
    joiner = input("Introduce a joiner from this set: ( !@#$%^&*_-=+?.,~;: ) (or leave a space): ")
    password_final = ""

    if isnan(int(number_of_words)):
        raise TypeError("Introduce a valid number")
    else:
        password_initial = generator.create_password_from_given_length(int(number_of_words), joiner)

    ans_cap = checker("capitalized")
    if ans_cap == 1:  # 1 for yes
        password_final = capitalizer_menu(password_initial)
        print("Your new password is: " + password_final)
        print("")
    elif ans_cap == 2:  # 2 for no
        password_final = password_initial
        print("Your new password is: " + password_final)
        print("")

    ans_ent = checker("entropy")
    if ans_ent == 1:  # 1 for yes
        entropy = entropycalculator.calculator(password_final)
        print("Entropy is: " + str(entropy))

    ans_hash = checker("hashing")
    if ans_hash == 1:  # 1 for yes
        hash_type, hashed_password = hashing_menu(password_final)
        print("Your " + hash_type + " hash is " + hashed_password)
