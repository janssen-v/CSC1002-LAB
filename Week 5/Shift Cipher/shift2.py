# Return the character after "value" positions
def shift(ch, value):
    if ch.isalpha() and ch.isupper():
        val = ord(ch) + value
        if val > ord('Z'): # Makes it work for Z, because otherwise it would be larger than the ascii limit
            val -= 2
        elif val < ord('A'): # Somehow this and the previous one doesn't work
            val += 2
        return chr(val)
    return ch
while True:
    ch = input('Enter a letter: ')
    print(ch, shift(ch,2))