from math import log2, pow

TOTAL_CHARSET = 70

CHARSET = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "=", "+", "?", ".", ",", "~", ";", ":"]


def calculator(password):
    length = len(password)
    r = TOTAL_CHARSET

    entropy = log2(pow(r, length))
    return entropy
