//
// Created by Joseph on 23/11/2019.
//

#ifndef CCIPHER_NGRAMS_H
#define CCIPHER_NGRAMS_H

#include <string>
#include <unordered_map>
#include <vector>


std::unordered_map<std::string, int> load_ngrams(const std::string& filename);
std::vector<int> load_ngrams_count(const std::unordered_map<std::string, int>& ngrams);
std::unordered_map<std::string, int> generate_ngrams(const std::string& text, int n);

class ngram_comparison {
public:
    ngram_comparison(const std::unordered_map<std::string, int> &realNgrams, int n);
    float compare(std::string text);
private:
    std::vector<int> desired_counts;
    int n;
};

#endif //CCIPHER_NGRAMS_H
