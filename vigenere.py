import re
import operator
import string

import affine
import utils

letters = string.ascii_lowercase

NORMAL_IOC = 0.0686

def most_likely_codeword_lengths(text):
    text = re.sub(utils.EXCEPT_LOWER_ALPHABET, '', text)

    # 20 is pretty long, but still reasonable
    average_iocs = {}
    for length in range(1, 21):
        summed_ioc = 0

        texts_to_analyse = split_text(text, length)
        for text_to_analyse in texts_to_analyse:
            summed_ioc += utils.index_of_coincidence(text_to_analyse)

        average_iocs[length] = summed_ioc/length
    
    # 5 seems good
    closest_iocs = sorted(average_iocs.items(), key=lambda t: 1/abs(t[1]-NORMAL_IOC), reverse=True)[:5]
    for key, value in closest_iocs:
        print(f'{key}: ioc = {value}')


def split_text(text, codeword_length):
    return [text[i::codeword_length] for i in range(codeword_length)]

def brute_vigenere(ciphertext, codeword_length, overrides={}):
    # This assumes a caesar cipher
    # Overrides should be a dictionary of index: override value values. The override value is the "place" of how common 'e' is in that shift. 1 means it is the most common, 2 second most, etc.
    # TODO, make this automatic
    ciphertext = re.sub(utils.EXCEPT_LOWER_ALPHABET, '', ciphertext)

    text_chunks = split_text(ciphertext, codeword_length)

    deciphered_text_chunks = []
    for i, chunk in enumerate(text_chunks):
        frequency_analysis = utils.frequency_analyse(chunk)
        probably_e = sorted(frequency_analysis.items(), key=lambda key: frequency_analysis[key[0]])[-1 if i not in overrides.keys() else -overrides[i]][0]

        print(probably_e)
        
        # 4 is e's index
        shift = letters.index(probably_e) - 4

        deciphered_text_chunks.append(affine.decipher(chunk, 1, shift))

    plaintext = ''
    i = -1
    while True:
        i += 1
        try:
            for j in range(codeword_length):
                plaintext += deciphered_text_chunks[j][i]
        except IndexError:
            break

    i = -1
    while True:
        i += 1
        try:
            for j in range(codeword_length):
                print(deciphered_text_chunks[j][i], end='')
            print('')
        except IndexError:
            break
