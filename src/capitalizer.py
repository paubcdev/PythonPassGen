import random


def randomize_upper_case_in_password(passw):  # This function takes the password as input and randomly capitalizes a
    # word in the string
    random_capitalized = ''.join(random.choice((str.upper, str.lower))(char) for char in passw)
    return random_capitalized


def upper_case_in_password(passw):  # This function takes the password as input and capitalizes all characters in it
    all_capitalized = passw.upper
    return all_capitalized


def capitalizer(password_initial, capitalized):
    if capitalized == 1:
        password_final = randomize_upper_case_in_password(password_initial)
        return print("Your new password is: " + password_final)

    elif capitalized == 2:
        password_final = upper_case_in_password(password_initial)
        return print("Your new password is: " + password_final)
