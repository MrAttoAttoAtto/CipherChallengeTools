import string
import re
from collections import Counter

EXCEPT_LOWER_ALPHABET = re.compile('[^a-z]')

letters = string.ascii_lowercase

def frequency_analyse(text):
    # Returns letter: percentage

    stripped_text = re.sub(EXCEPT_LOWER_ALPHABET, '', text)
    counted_items = Counter(stripped_text)
    char_count = len(stripped_text)

    return {letter: count/char_count*100 for letter, count in dict(counted_items).items()}
    
    #for letter, count in sorted(dict(counted_items).items()):
    #    print(f'{letter}: {count/char_count*100:.2f}% occurrence rate')

def index_of_coincidence(text):
    stripped_text = re.sub(EXCEPT_LOWER_ALPHABET, '', text)
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