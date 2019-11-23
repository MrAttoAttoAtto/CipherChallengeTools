//
// Created by Joseph on 23/11/2019.
//

#include <boost/algorithm/string.hpp>
#include <boost/regex.hpp>
#include <fstream>
#include "treatment.h"

void treat(std::string &text) {
    boost::to_lower(text);
    boost::regex expr{"[^a-z]"};
    std::string fmt;
    text = boost::regex_replace(text, expr, fmt);
}

std::string read_file(const std::string &filename) {
    std::ifstream file;
    file.open(filename);
    if (!file.is_open()) {
        throw std::runtime_error("Cannot open file");
    }
    std::string contents;
    file.seekg(0, std::ios::end);
    contents.resize(file.tellg());
    file.seekg(0, std::ios::beg);
    file.read(&contents[0], contents.size());
    file.close();
    return(contents);
}
