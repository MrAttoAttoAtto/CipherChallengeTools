//
// Created by Joseph on 23/11/2019.
//

#include "ngrams.h"
#include <fstream>
#include <math.h>
#include <iostream>
#include "../stats/distribution.h"

#include <boost/algorithm/string.hpp>

std::unordered_map<std::string, int> load_ngrams(const std::string& filename) {
    std::string line;
    std::unordered_map<std::string, int> ngrams;
    std::string key;
    int count;

    std::ifstream file;
    file.open(filename);
    if (file.is_open()) {
        while (!file.eof()) {
            file >> key;
            file >> count;
            boost::to_lower(key);
            ngrams[key] = count;
        }
        file.close();
    } else {
        throw std::runtime_error("Failed to open file.");
    }
    return ngrams;
}

std::vector<int> load_ngrams_count(const std::unordered_map<std::string, int>& ngrams) {
    std::vector<int> retval;
    retval.reserve(ngrams.size());
    for (auto &p : ngrams) {
        retval.push_back(p.second);
    }
    return retval;
}

std::unordered_map<std::string, int> generate_ngrams(const std::string &text, int n) {
    std::unordered_map<std::string, int> ngrams;
    std::unordered_map<std::string, int>::iterator it;
    std::string temp;
    for (int i = 0; i < text.size() - n; i++) {
        temp = text.substr(i, n);
        it = ngrams.find(temp);
        if (it != ngrams.end()) {
            ngrams[temp]++;
        } else {
            ngrams[temp] = 1;
        }
    }
    return ngrams;
}

float ngram_comparison::compare(std::string text) {
    auto sample = load_ngrams_count(generate_ngrams(text, n));
    auto c_sample = cumulative_probabilities_counts(sample);
    std::vector<int> trimmed_reference(desired_counts.end() - std::min(desired_counts.size(), sample.size()), desired_counts.end());
    auto c_ref = cumulative_probabilities_counts(trimmed_reference);
    float val = kolmogorov_smirnov_stat(c_ref, c_sample);
    float ks_threshold = 1.517 * std::sqrt((float) (2*c_ref.size()) / (float) (c_ref.size()*c_ref.size()));
    return ks_threshold - val;
}

ngram_comparison::ngram_comparison(const std::unordered_map<std::string, int> &realNgrams, int n) :n(n) {
    desired_counts = load_ngrams_count(realNgrams);
    std::sort(desired_counts.begin(), desired_counts.end());
}
