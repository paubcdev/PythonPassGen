# import math

ALPHABET_UNDERCASE = 26
ALPHABET_UPPERCASE = 26
SYMBOLS = 19

charset = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "=", "+", "?", ".", ",", "~", ";", ":"]


check = False
while not check:
    char = input("Introduce a symbol: ")
    if char in charset:
        print("It is present.")
        check = True
    else:
        print("It is not present.")
        check = False

"!"  # exclamation
"@"  # at
"#"  # hashtag
"$"  # dollar
"%"  # percent
"^"  # up
"&"  # ampersand
"*"  # asterisk
" "  # space
"+"  # plus
"="  # equal
"-"  # hyphen
"_"  # underscore
"?"  # question
"~"  # tilde
"."  # dot
","  # comma
":"  # colon
";"  # semicolon
