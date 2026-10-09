#include "generators.hpp"
#include <random>
#include <numeric>
#include <algorithm>

std::vector<int> generate_exp1_data(int64_t n, uint32_t seed) {
    std::vector<int> arr(n);
    std::mt19937_64 gen(seed);
    std::uniform_int_distribution<int> dis(0, static_cast<int>(n - 1));
    for (int64_t i = 0; i < n; ++i) {
        arr[i] = dis(gen);
    }
    return arr;
}

std::vector<int> generate_exp2_data(int64_t n, int64_t k, uint32_t seed) {
    std::vector<int> arr(n);
    std::iota(arr.begin(), arr.end(), 0); // 0 to n-1
    std::mt19937_64 gen(seed);
    std::uniform_int_distribution<int64_t> dis(0, n - 1);
    for (int64_t i = 0; i < k; ++i) {
        int64_t p1 = dis(gen);
        int64_t p2 = dis(gen);
        std::swap(arr[p1], arr[p2]);
    }
    return arr;
}

std::vector<int> generate_exp3_data(int64_t n, int64_t k, uint32_t seed) {
    std::vector<int> arr(n);
    std::mt19937_64 gen(seed);
    std::uniform_int_distribution<int> dis(0, static_cast<int>(k - 1));
    for (int64_t i = 0; i < n; ++i) {
        arr[i] = dis(gen);
    }
    return arr;
}
