import string

letters = string.ascii_lowercase

multiplicative_inverses = [
    1,0,
    9,0,
    21,0,
    15,0,
    3,0,
    19,0,
    0,0,
    7,0,
    23,0,
    11,0,
    5,0,
    17,0,
    25,0
]

def encipher(plaintext, multiplier, constant):
    ciphertext = ''
    for char in plaintext:
        char_pos = letters.index(char)+1
        new_char_pos = (char_pos*multiplier + constant - 1) % 26
        ciphertext += letters[new_char_pos]
    
    return ciphertext

def decipher(ciphertext, multiplier, constant):
    plaintext = ''
    for char in ciphertext:
        try:
            char_pos = letters.index(char)+1
        except ValueError:
            plaintext += char
            continue
        multiplicative_inverse = multiplicative_inverses[multiplier-1]
        new_char_pos = (multiplicative_inverse*(char_pos-constant)-1) % 26
        plaintext += letters[new_char_pos]

    return plaintext
