import affine

possible_multipliers = [1,3,5,7,9,11,15,17,19,21,23,25]

words = ["the", "and", "secret"]

def brute_ciphertext(ciphertext):
    ciphertext = ciphertext.lower()

    for multiplier in possible_multipliers:
        for constant in range(26):
            #print(affine.decipher(ciphertext, multiplier, constant).lower())
            plaintext = affine.decipher(ciphertext, multiplier, constant).lower()
            if all(word in plaintext for word in words):
                # Fix later
                print(f"Possibly: x->{multiplier}x+{constant}")
                print(affine.decipher(ciphertext, multiplier, constant).lower())