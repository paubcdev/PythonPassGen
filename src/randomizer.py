import random


def randomize_upper_case_in_password(passw):  # This function takes the password as input and randomly
    # capitalizes a word in the string
    password_final = ''.join(random.choice((str.upper, str.lower))(char) for char in passw)
    return password_final


def upper_case_first_letter(passw):
    pass


def random_capitalizer(password_initial):
    cap_done = 0
    while cap_done == 0:
        capitalized = input("Do you want it capitalized? (Y/N): ")

        if capitalized == 'Y':
            password_capitalized = randomize_upper_case_in_password(password_initial)
            cap_done = 1
            return print("Your new password is: " + password_capitalized)

        elif capitalized == 'y':
            password_capitalized = randomize_upper_case_in_password(password_initial)
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
