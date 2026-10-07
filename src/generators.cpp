#include "generators.hpp"
#include <random>
#include <numeric>
#include <algorithm>

std::vector<int> generate_exp1_data(size_t n, int seed) {
    std::vector<int> arr(n);
    std::mt19937 gen(seed);
    std::uniform_int_distribution<> dis(0, n - 1);
    for (size_t i = 0; i < n; ++i) {
        arr[i] = dis(gen);
    }
    return arr;
}

std::vector<int> generate_exp2_data(size_t n, int k, int seed) {
    std::vector<int> arr(n);
    std::iota(arr.begin(), arr.end(), 0); // 0 to n-1
    std::mt19937 gen(seed);
    std::uniform_int_distribution<> dis(0, n - 1);
    for (int i = 0; i < k; ++i) {
        int p1 = dis(gen);
        int p2 = dis(gen);
        std::swap(arr[p1], arr[p2]);
    }
    return arr;
}

std::vector<int> generate_exp3_data(size_t n, int k, int seed) {
    std::vector<int> arr(n);
    std::mt19937 gen(seed);
    std::uniform_int_distribution<> dis(0, k - 1);
    for (size_t i = 0; i < n; ++i) {
        arr[i] = dis(gen);
    }
    return arr;
}
