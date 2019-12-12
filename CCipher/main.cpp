#include <iostream>
#include <algorithm>


#include "stats/distribution.h"
#include "textutils/ngrams.h"
#include "textutils/treatment.h"
#include "ciphers/transposition.h"


int main(int argc, char* argv[]) {
    std::cout << "Hello, World!" << std::endl;
    auto eng_ngrams = load_ngrams("english_trigrams.txt");
    ngram_comparison ngramComparison(eng_ngrams, 3);
    auto ctext = read_file("ciphertext.txt");
    treat(ctext);
    int c = 7;
    if (argc > 1) {
        c = strtol(argv[1], nullptr, 0);
    }
    brute_force(ctext, false, ngramComparison, c);
    return 0;
}