import os
import random
import secrets


def create_password_from_given_length(leng, joinr):  # This function takes a number and a joiner type as inputs,
    # iterates that number of times from wordlist, takes one randomly, introduces a number after it, then appends
    # it to a password variable and then returns it, with the type of joiner selected
    if os.name == 'posix':  # if the OS is UNIX-based, takes the wordlist contained in the usr directory
        with open('/usr/share/dict/words') as wordlist:
            words = [word.strip() for word in wordlist]
    else:  # if the OS is not UNIX-based, then an alternate wordlist is provided
        with open('support_files/words') as wordlist:
            words = [word.strip() for word in wordlist]
    password = joinr.join(secrets.choice(words) + str(random.randint(0, 9)) for _ in range(leng))
    return password
