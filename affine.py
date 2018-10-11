import string
import math

letters = string.ascii_lowercase

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



def encipher(plaintext, multiplier, constant):
    ciphertext = ''
    for char in plaintext:

        # In order that any character can be enciphered, but only lowercase letters are modified
        try:
            char_pos = letters.index(char)
        except ValueError:
            ciphertext += char
            continue

        new_char_pos = (char_pos*multiplier + constant) % 26
        ciphertext += letters[new_char_pos]
    
    return ciphertext

def decipher(ciphertext, multiplier, constant):
    plaintext = ''
    for char in ciphertext:
        try:
            char_pos = letters.index(char)
        except ValueError:
            plaintext += char
            continue

        multiplicative_inverse = modinv(multiplier, 26) 
        new_char_pos = (multiplicative_inverse*(char_pos-constant)) % 26
        plaintext += letters[new_char_pos]

    return plaintext


def get_results_of_linear_congruence(a, b, m):
    # Gives all solutions to ax = b (mod m)

    gcd = math.gcd(a, m)

    if b % gcd != 0:
        raise Exception("This linear congruence has no solutions")
    elif gcd == 1:
        return set([(b*modinv(a, m)) % m])
    
    reduced_a = a//gcd
    reduced_b = b//gcd
    reduced_m = m//gcd

    # This can be helped solved by solving my = -b (mod a)
    y_results = get_results_of_linear_congruence(reduced_m, -reduced_b, reduced_a)

    all_results = set()
    for y in y_results:
        # x = (m*y + b)/a
        base_x = (m*y + b)//a
        for x in range(base_x, m, reduced_m):
            all_results.add(x)
    
    return all_results


def calculate_keys(character1, character1mapping, character2, character2mapping):
    # Takes the mappings of two characters and outputs the key such a transformation corresponds to
    # Character1 and 2 are ENCIPHERED, the others are the (purported) DECIPHERED versions of both

    character1_index = letters.index(character1)
    character2_index = letters.index(character2)
    character1mapping_index = letters.index(character1mapping)
    character2mapping_index = letters.index(character2mapping)

    # Character1mapping index * a + b = character1 index mod 26
    # Same for character2
    # let character1mapping index * a = no_constant_value mod 26

    # (Character1mapping index-Character2mapping index)*a = (character1 index-character2 index) mod 26
    # difference*a = resultant_difference mod 26

    difference = character1mapping_index - character2mapping_index
    resultant_difference = (character1_index-character2_index) % 26

    if difference < 0:
        difference = abs(difference)
        resultant_difference = -resultant_difference % 26

    # If we just assumed a = resultant_difference/difference, we would be forgetting about the mod 26 and probably getting a decimal
    # So instead we need to find all a where difference*a = resultant_difference mod 26

    multiplier_possibilities = get_results_of_linear_congruence(difference, resultant_difference, 26)

    for multiplier in multiplier_possibilities:
        if multiplier not in [1,3,5,7,9,11,15,17,19,21,23,25]:
            # Others would be ambiguous solutions
            continue

        no_constant_value = (character1mapping_index*multiplier) % 26
        constant = (character1_index-no_constant_value) % 26

        print(f"x->{multiplier}x+{constant}")
