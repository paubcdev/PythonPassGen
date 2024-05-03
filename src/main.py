import random
import secrets
import math


class PasswordClass:
    @staticmethod
    def create_password_from_given_length(leng, joinr):  # This function takes a number and a joiner type as inputs,
        # iterates that number of times from wordlist, takes one randomly, introduces a number after it, then appends
        # it to a password variable and then returns it, with the type of joiner selected
        with open('words') as wordlist:
            words = [word.strip() for word in wordlist]
            password = joinr.join(secrets.choice(words) + str(random.randint(0, 9)) for _ in range(leng))
        return password

    @staticmethod
    def randomize_upper_case_in_password(passw):  # This function takes the password as input and randomly
        # capitalizes a word in the string
        password_final = ''.join(random.choice((str.upper, str.lower))(char) for char in passw)
        return password_final


number_of_words = input("Introduce number of words for password: ")
joiner = input("Introduce a joiner (or leave a space, or blank for no joiner): ")

if math.isnan(int(number_of_words)):
    raise TypeError("Introduce a valid number")
else:
    password_initial = PasswordClass.create_password_from_given_length(int(number_of_words), joiner)

done = 0
while done == 0:
    capitalized = input("Do you want it capitalized? Please select Y/N: ")

    if capitalized == 'Y':
        password_capitalized = PasswordClass.randomize_upper_case_in_password(password_initial)
        print("Your new password is: " + password_capitalized)
        done = 1

    elif capitalized == 'y':
        password_capitalized = PasswordClass.randomize_upper_case_in_password(password_initial)
        print("Your new password is: " + password_capitalized)
        done = 1

    elif capitalized == 'N':
        print("Your new password is: " + password_initial)
        done = 1

    elif capitalized == 'n':
        print("Your new password is: " + password_initial)
        done = 1

    else:
        print("Error! Please select a correct option.")
        done = 0
