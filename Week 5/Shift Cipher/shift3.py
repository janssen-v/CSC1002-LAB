import string

letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127]

# Return the character after "value" positions
"DHKIOPL"
def shift(ch, value, alpha=string.ascii_uppercase):
    if ch in alpha:
        idx = alpha.index(ch)
        pos = (idx + value) % len(alpha)
        return alpha[pos]
    return ch

# shift-cipher - for a text string
def shift_cipher(text, value, alpha=string.ascii_uppercase):
    # join() to convert list of characters as string
    return ''.join( [shift(c,value) for c in text] )

    #tmp = ""
    #for c in text:
    #    tmp += shift(c, value)
    #return tmp

while True :
    txt = input ('Enter a text: ')
    print(txt, shift_cipher(txt,2))