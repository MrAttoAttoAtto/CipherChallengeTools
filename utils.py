import string
import re
from math import log
from collections import Counter

frequency_english = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "l", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j", "q", "z"]

EXCEPT_LOWER_ALPHABET = re.compile('[^a-z0-9]')

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

def block_ngrams(text, n):
    ngs = {}
    for i in range(0, len(text)-(n-1), n):
        ng = text[i:i+n]
        if ngs.get(ng) is None:
            ngs[ng] = 1
        else:
            ngs[ng] += 1
    
    return sorted(ngs.items(), key=lambda x: x[1], reverse=True)

def ngrams(text, n):
    ngs = {}
    for i in range(0, len(text)-(n-1)):
        ng = text[i:i+n]
        if ngs.get(ng) is None:
            ngs[ng] = 1
        else:
            ngs[ng] += 1
    
    return sorted(ngs.items(), key=lambda x: x[1], reverse=True)

def reinsert_chars(plaintext, extra_chars):
    pt_list = list(plaintext)
    for char_item in extra_chars:
        pt_list.insert(char_item[1], char_item[0])
    
    return ''.join(pt_list)

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).

def infer_spaces(s):
    words = open("words.txt").read().split()
    wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
    maxword = max(len(x) for x in words)

    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))