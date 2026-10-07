#ifndef UTILS_HPP
#define UTILS_HPP

#include <vector>
#include <string>
#include <chrono>
#include <fstream>
#include <iostream>
#include <algorithm>

class Timer {
    using clock_t = std::chrono::steady_clock;
    using timepoint_t = clock_t::time_point;
    timepoint_t start_time;
public:
    void start() { start_time = clock_t::now(); }
    double elapsed_seconds() {
        timepoint_t end_time = clock_t::now();
        std::chrono::duration<double> diff = end_time - start_time;
        return diff.count();
    }
};

inline void verify_sorted(const std::vector<int>& arr) {
    if (!std::is_sorted(arr.begin(), arr.end())) {
        std::cerr << "Error: Array is NOT sorted!" << std::endl;
        std::exit(1);
    }
}

#endif // UTILS_HPP
