#ifndef GENERATORS_HPP
#define GENERATORS_HPP

#include <vector>
#include <cstdint>

// Data generators for 3 experiments
std::vector<int> generate_exp1_data(int64_t n, uint32_t seed);
std::vector<int> generate_exp2_data(int64_t n, int64_t k, uint32_t seed);
std::vector<int> generate_exp3_data(int64_t n, int64_t k, uint32_t seed);

#endif // GENERATORS_HPP
