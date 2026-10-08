#ifndef GENERATORS_HPP
#define GENERATORS_HPP

#include <vector>
#include <cstddef>

// Data generators for 3 experiments
std::vector<int> generate_exp1_data(size_t n, int seed);
std::vector<int> generate_exp2_data(size_t n, int k, int seed);
std::vector<int> generate_exp3_data(size_t n, int k, int seed);

#endif // GENERATORS_HPP

