//
// Created by Joseph on 23/11/2019.
//

#ifndef CCIPHER_DISTRIBUTION_H
#define CCIPHER_DISTRIBUTION_H

#include <vector>
std::vector<float> cumulative_probabilities_counts(std::vector<int> &counts);
float kolmogorov_smirnov_stat(std::vector<float> a, std::vector<float> b);


#endif //CCIPHER_DISTRIBUTION_H
