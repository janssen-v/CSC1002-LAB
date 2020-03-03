# Shift a letter
# ord() -> returns the ascii value of the given letter
# chr() -> returns the letter from a given ascii value

val = 4
letter ='A'

while True:
    ch = input('Enter a letter : ')
    print(ord(ch), chr(ord(ch)+val))