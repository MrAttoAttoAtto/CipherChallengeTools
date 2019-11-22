import affine
import keywords as ke
import transposition
import itertools

possible_multipliers = [1,3,5,7,9,11,15,17,19,21,23,25]

def brute_time(ciphertext, k, lword):
    ciphertext = ciphertext.lower()

    for i, word in enumerate(ke.read_words()):
        #if any(letter in word for letter in ["k", "l", "m", "n", "d"]):
        #    continue

        if len(word) > 9:
            continue

        half_plaintext = ke.decipher(ciphertext, word)

        transposition.LIKELY_WORDS = [lword]

        x = transposition.try_find_anagram(half_plaintext, k)
        if len(x[0]):
            plain = transposition.decrypt_rows(half_plaintext, x[0])
            if lword in plain:
                print(word)
                print(x)
                print(plain)
            