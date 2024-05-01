from random import choice as ranchoice, randint
from secrets import choice as secchoice
import math


class PasswordClass:
    @staticmethod
    def create_password_from_given_lentgh(leng, joinr):  # This function takes a number and a joiner type as inputs,
        # iterates that number of times from wordlist, takes one randomly, introduces a number after it, then appends
        # it to a password variable and then returns it, with the type of joiner selected
        with open('words') as wordlist:
            words = [word.strip() for word in wordlist]
            password = joinr.join(secchoice(words) + str(randint(0, 9)) for _ in range(leng))
        return password

    @staticmethod
    def randomize_upper_case_in_password(passw):  # This function takes the password as input and randomly
        # capitalizes a word in the string
        password_final = ''.join(ranchoice((str.upper, str.lower))(char) for char in passw)
        return password_final


number_of_words = input("Introduce number of words for password: ")
joiner = input("Introduce a joiner (or leave a space, or blank for no joiner): ")
if math.isnan(int(number_of_words)):
    raise TypeError("Introduce a valid number")
else:
    password_initial = PasswordClass.create_password_from_given_lentgh(int(number_of_words), joiner)
    print(password_initial)

password_capitalize = PasswordClass.randomize_upper_case_in_password(password_initial)
print(password_capitalize)
