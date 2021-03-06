import string
import re
import utils

EXCEPT_LOWER_ALPHABET = re.compile('[^a-z]')

letters = string.ascii_lowercase

def read_words():
    with open("./100k-words.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    words = text.split("\n")
    fixed_words = [re.sub(EXCEPT_LOWER_ALPHABET, "", word.lower()) for word in words if not word.startswith("#")]

    return fixed_words

def make_mapping(keyword):
    mapping = ""
    for letter in keyword:
        if letter not in mapping:
            mapping += letter
    
    last_letter_index = letters.index(mapping[-1])
    offset = 1
    for i in range(26-len(mapping)):
        while letters[(i+last_letter_index+offset) % 26] in mapping:
            offset += 1
        
        mapping += letters[(i+last_letter_index+offset) % 26]
    
    return mapping

def make_back_mapping_dict(keyword):
    mapping = make_mapping(keyword)

    mapping_dict = {}
    for i in range(26):
        mapping_dict[mapping[i]] = letters[i]
    
    return mapping_dict

def decipher(ciphertext, keyword, human=False, include_extra_chars=False):
    ciphertext = ciphertext.lower()

    if include_extra_chars:
        extra_chars = [[m.group(0), m.start(0)] for m in re.finditer(utils.EXCEPT_LOWER_ALPHABET, ciphertext)]
    else:
        extra_chars = []

    ciphertext = re.sub(EXCEPT_LOWER_ALPHABET, "", ciphertext)

    back_mapping = make_back_mapping_dict(keyword)
    plaintext = ""

    for letter in ciphertext:
        plaintext += back_mapping[letter]

    if include_extra_chars:
        plaintext = utils.reinsert_chars(plaintext, extra_chars)

    if human:
        keyword = ""

        for letter in letters:
            for mapped, original in back_mapping.items():
                if original == letter:
                    keyword += mapped
        plaintext += f'\n\n{string.ascii_lowercase}\n{keyword}'

    return plaintext

def brute_keyword(ciphertext, likely_words=[]):
    ciphertext = ciphertext.lower()
    ciphertext = re.sub(EXCEPT_LOWER_ALPHABET, "", ciphertext)

    words_to_check = ["the", "and", "of", "to", "in", "at"] + likely_words

    for i, word in enumerate(read_words()):
        #if any(letter in word for letter in ["k", "l", "m", "n", "d"]):
        #    continue

        plaintext = decipher(ciphertext, word)

        if i % 1000 == 0:
            print(i)

        if all(word in plaintext for word in words_to_check):
            print(plaintext)

            mapping = make_mapping(word)
            print("\n"+letters+"\n"+mapping)

def frequency_guess(ciphertext, human=True):
    ciphertext = ciphertext.lower()
    ciphertext = re.sub(EXCEPT_LOWER_ALPHABET, "", ciphertext)

    freq = utils.frequency_analyse(ciphertext)

    sorted_freq = [tup[0] for tup in sorted(freq.items(), key=lambda x: x[1], reverse=True)]
    for letter in letters:
        if letter not in sorted_freq:
            sorted_freq.append(letter)


    back_mapping = {}
    for i in range(26):
        back_mapping[sorted_freq[i][0]] = utils.frequency_english[i]
    
    plaintext = ""

    for letter in ciphertext:
        plaintext += back_mapping[letter]
    
    if human:
        keyword = ""

        for letter in letters:
            for mapped, original in back_mapping.items():
                if original == letter:
                    keyword += mapped
        
        plaintext += f"\n{letters}\n{keyword}"
    
    return plaintext
