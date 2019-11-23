#include <iostream>
#include <algorithm>


#include "stats/distribution.h"
#include "textutils/ngrams.h"
#include "textutils/treatment.h"
#include "ciphers/transposition.h"


int main() {
    std::cout << "Hello, World!" << std::endl;
    auto eng_ngrams = load_ngrams("english_trigrams.txt");
    ngram_comparison ngramComparison(eng_ngrams, 3);
    auto ctext = read_file("ciphertext.txt");
    treat(ctext);

    brute_force(ctext, false, ngramComparison);
    return 0;
}