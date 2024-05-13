from math import log2, pow

TOTAL_CHARSET = 70

CHARSET = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "=", "+", "?", ".", ",", "~", ";", ":"]


def calculator(password):
    length = len(password)
    r = TOTAL_CHARSET

    entropy = log2(pow(r, length))
    return entropy



'''
check = False
while not check:
    char = input("Introduce a symbol: ")
    if char in CHARSET:
        print("It is present.")
        check = True
    else:
        print("It is not present.")
        check = False
'''