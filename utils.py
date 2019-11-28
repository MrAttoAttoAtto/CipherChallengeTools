import string
import re
from collections import Counter

frequency_english = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "l", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j", "q", "z"]

EXCEPT_LOWER_ALPHABET = re.compile('[^a-z]')

letters = string.ascii_lowercase

def frequency_analyse(text, human=False):
    # Returns letter: percentage

    stripped_text = re.sub(EXCEPT_LOWER_ALPHABET, '', text)
    counted_items = Counter(stripped_text)
    char_count = len(stripped_text)
    
    if human:
        for letter, count in sorted(dict(counted_items).items()):
            print(f'{letter}: {count/char_count*100:.2f}% occurrence rate')
    else:
        return {letter: count/char_count*100 for letter, count in dict(counted_items).items()}

def index_of_coincidence(text):
    stripped_text = re.sub(EXCEPT_LOWER_ALPHABET, '', text.lower())
    counted_items = Counter(stripped_text)
    char_count = len(stripped_text)

    ioc = 0
    for letter, count in dict(counted_items).items():
        ioc += (count**2-count)/(char_count**2-char_count)

    return ioc

def columnify(text, width):
    columns = []
    for i in range(0, len(text), width):
        chunk = ''
        for j in range(i, i+width):
            try:
                chunk += text[j]
            except IndexError:
                break
        
        columns.append(chunk)

    return columns

def chunkify(text, n):
    return [text[i:i+n] for i in range(0, len(text), n)]

def reinsert_chars(plaintext, extra_chars):
    pt_list = list(plaintext)
    for char_item in extra_chars:
        pt_list.insert(char_item[1], char_item[0])
    
    return ''.join(pt_list)