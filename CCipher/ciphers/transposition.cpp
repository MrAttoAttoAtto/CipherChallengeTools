//
// Created by Joseph on 23/11/2019.
//

#include <algorithm>
#include <iostream>
#include "transposition.h"
#include "../textutils/ngrams.h"
#include <boost/timer/timer.hpp>
std::string rows_from_columns(std::string text, int n) {
    std::string result(text.size(), ' ');
    int std_col_len = text.size()/n;
    int extra_cols = text.size() % n;

    // a Zip Implementation - Not cache sensitive but cross fingers
    int string_index = 0;
    // Column Number
    for (int i = 0; i < n; i++) {
        int col_len = i < extra_cols ? std_col_len+1 : std_col_len;
        // No in column(going downwards)
        for (int j = 0; j < col_len; j++) {
            result[i + j*n] = text[string_index++];
        }
    }
    return result;
}

std::string decipher(std::string text, std::vector<int> order, bool columnar) {
    int col_n = order.size();
    int row_n = (text.size()+col_n-1) / col_n;
    std::string result;
    result.reserve(text.size());
    if (columnar) {
        text = rows_from_columns(text, col_n);
    }
    // Every row(except last)
    for (int i = 0; i < (row_n - 1); i++) {
        for (int pos: order) {
            result += text[i*col_n + pos];
        }
    }
    // Pay extra attention to last row
    for (int pos: order) {
        if (((row_n-1)*col_n + pos) < text.size()) {
            result += text[(row_n-1)*col_n + pos];
        }
    }
    return result;
}

std::string brute_force(std::string text, bool columnar, ngram_comparison ngramComparison) {
    std::vector<int> curr_order{0,1,2};
    for (int n = 3; n < 13; n++) {
        boost::timer::auto_cpu_timer t;
        std::cout << n << std::endl;
        std::sort(curr_order.begin(), curr_order.end());
        std::string plain;
        do {
            plain = decipher(text, curr_order, columnar);
            float c = ngramComparison.compare(plain);
            if (c > 0) {
                std::cout << plain.substr(0, 20) << " " << c << std::endl;
            }
        } while (std::next_permutation(curr_order.begin(), curr_order.end()));
        curr_order.push_back(curr_order.size());
    }
    return "";
}
