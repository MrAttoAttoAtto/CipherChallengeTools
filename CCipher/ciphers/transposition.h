//
// Created by Joseph on 23/11/2019.
//

#ifndef CCIPHER_TRANSPOSITION_H
#define CCIPHER_TRANSPOSITION_H

#include <string>
#include <vector>
#include "../textutils/ngrams.h"


std::string rows_from_columns(std::string text, int n);
std::string decipher(std::string text, const std::vector<int> &order, bool columnar);
std::string brute_force(std::string text, bool columnar, ngram_comparison ngramComparison, int max_length);

#endif //CCIPHER_TRANSPOSITION_H
