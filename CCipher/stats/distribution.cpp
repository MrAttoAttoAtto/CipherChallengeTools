//
// Created by Joseph on 23/11/2019.
//


#include "distribution.h"
#include <stdexcept>
#include <algorithm>
#include "../textutils/ngrams.h"


float kolmogorov_smirnov_stat(std::vector<float> a, std::vector<float> b) {
    if (a.size() != b.size()) {
        throw std::runtime_error("Cannot compare unequal size datasets.");
    }
    float max_diff = 0;
    for (size_t i = 0; i < a.size(); ++i) {
        float diff = std::abs(a[i] - b[i]);
        if (diff > max_diff) {
            max_diff = diff;
        }
    }
    return max_diff;
}

std::vector<float> cumulative_probabilities_counts(std::vector<int> &counts) {
    std::sort(counts.begin(), counts.end());
    float sum = 0;
    for (auto c:counts)
        sum += c;
    std::vector<float> retval(counts.size(), 0);
    int max = counts[counts.size()-1];
    float last_val = 0;
    for (size_t i = 0; i < counts.size(); ++i) {
        retval[i] = last_val = last_val + ((float) counts[i]/ sum);
    }
    return retval;
}
