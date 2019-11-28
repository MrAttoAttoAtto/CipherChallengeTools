cmake_minimum_required(VERSION 3.12)
project(CCipher)

find_package(Boost REQUIRED COMPONENTS regex timer)

set(CMAKE_CXX_STANDARD 11)

add_executable(CCipher main.cpp stats/distribution.cpp stats/distribution.h textutils/ngrams.cpp textutils/ngrams.h textutils/treatment.cpp textutils/treatment.h ciphers/transposition.cpp ciphers/transposition.h)

target_link_libraries(CCipher
        PRIVATE Boost::boost Boost::regex Boost::timer)