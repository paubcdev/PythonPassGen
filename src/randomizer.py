import random


def randomize_upper_case_in_password(passw):  # This function takes the password as input and randomly
    # capitalizes a word in the string
    password_final = ''.join(random.choice((str.upper, str.lower))(char) for char in passw)
    return password_final


def upper_case_first_letter(passw):
    pass
