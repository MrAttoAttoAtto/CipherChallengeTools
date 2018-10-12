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

def brute_vigenere(ciphertext, codeword_length, keywords=[], overrides=[]):
    # This assumes a caesar cipher
    # Overrides should be a dictionary of index: override value values. The override value is the "place" of how common 'e' is in that shift. 1 means it is the most common, 2 second most, etc.
    # -1 means it could be anything

    ciphertext = re.sub(utils.EXCEPT_LOWER_ALPHABET, '', ciphertext)

    text_chunks = split_text(ciphertext, codeword_length)

    deciphered_text_chunks = []
    shifts = []
    for i, chunk in enumerate(text_chunks):
        frequency_analysis = utils.frequency_analyse(chunk)

        sorted_frequency_analysis = sorted(frequency_analysis.items(), key=lambda key: frequency_analysis[key[0]])

        print(f'Chunk {i+1}: Most frequent: {sorted_frequency_analysis[-1][1]:.2f}%, Second: {sorted_frequency_analysis[-2][1]:.2f}%, Difference: {sorted_frequency_analysis[-1][1]-sorted_frequency_analysis[-2][1]:.2f}%')

        if not len(overrides) == codeword_length or -1 in overrides:
            deciphered_text_chunks.append([])
            shifts.append([])

            for e_frequency in [1,2,3]:
                probably_e = sorted_frequency_analysis[-e_frequency][0]
                
                # 4 is e's index
                shift = letters.index(probably_e) - 4
                shifts[i].append(shift)

                deciphered_text_chunks[i].append(affine.decipher(chunk, 1, shift))
        else:
            probably_e = sorted_frequency_analysis[-overrides[i]][0]
            
            # 4 is e's index
            shift = letters.index(probably_e) - 4
            shifts.append(shift)

            deciphered_text_chunks.append(affine.decipher(chunk, 1, shift))

    if len(overrides) == codeword_length and -1 not in overrides:
        plaintext = ''

        i = -1
        while True:
            i += 1
            try:
                for j in range(codeword_length):
                    plaintext += deciphered_text_chunks[j][i]
            except IndexError:
                break

        codeword = ''
        codeword_alter = ''
        for i in range(codeword_length):
            codeword += letters[shifts[i]-1]
            codeword_alter += letters[shifts[i]]
        
        print(f"E frequency places: {', '.join([str(e_frequency) for e_frequency in overrides])}\n{plaintext}\nCodeword: {codeword.upper()} or {codeword_alter.upper()}\n")
    else:
        recursive_combination(codeword_length, deciphered_text_chunks, keywords, overrides, shifts, [], codeword_length)


def recursive_combination(length, text_chunks, keywords, overrides, shifts, order, level):
    if level != 0:
        level -= 1
        recursive_combination(length, text_chunks, keywords, overrides, shifts, order + [0], level)
        recursive_combination(length, text_chunks, keywords, overrides, shifts, order + [1], level)
        recursive_combination(length, text_chunks, keywords, overrides, shifts, order + [2], level)
    else:
        # Makes sure that, if an override is set, only the ones satisfying the override work
        applicable = True
        if overrides and not order == [0]*length:
            for i in range(length):
                try:
                    if overrides[i] != order[i]+1 and overrides[i] != -1:
                        applicable = False
                except IndexError:
                    pass

        if not applicable:
            return

        plaintext = ''

        i = -1
        while True:
            i += 1
            try:
                for j in range(length):
                    plaintext += text_chunks[j][order[j]][i]
            except IndexError:
                break
        
        # If it's a possible plaintext (has certain words), or it's the one where E is the most common (for extended analysis)
        if all(word in plaintext for word in ["the", "of", "and", "to", "in", "is", "for", "that", "was", 'on', 'with', 'it'] + keywords) or order == [0]*length:
            '''columns = []
            for i in range(0, len(plaintext), length):
                chunk = ''
                for j in range(i, i+length):
                    try:
                        chunk += plaintext[j]
                    except IndexError:
                        break
                
                columns.append(chunk)

            backslash = '\n'
            print(f'E frequency places: {", ".join([str(e_frequency+1) for e_frequency in order])}\n{backslash.join(columns)}\n')'''

            codeword = ''
            codeword_alter = ''
            for i in range(length):
                codeword += letters[shifts[i][order[i]]-1]
                codeword_alter += letters[shifts[i][order[i]]]

            print(f'E frequency places: {", ".join([str(e_frequency+1) for e_frequency in order])}\n{plaintext}\nCodeword: {codeword.upper()} or {codeword_alter.upper()}\n')
