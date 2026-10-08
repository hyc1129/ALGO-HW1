#include "sorts.hpp"
#include "generators.hpp"
#include "utils.hpp"
#include <iostream>
#include <vector>
#include <string>
#include <functional>
#include <cstdlib>

int g_count_k = 0;
void counting_sort_wrapper(std::vector<int>& arr) {
    counting_sort(arr, g_count_k);
}

int main(int argc, char* argv[]) {
    int exp = 1;
    int trials = 10;
    int seed = 0;
    size_t n = 1024;
    int k = 1024;
    std::string algo_name = "Merge";

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--exp" && i + 1 < argc) exp = std::stoi(argv[++i]);
        else if (arg == "--trials" && i + 1 < argc) trials = std::stoi(argv[++i]);
        else if (arg == "--seed" && i + 1 < argc) seed = std::stoi(argv[++i]);
        else if (arg == "--n" && i + 1 < argc) n = std::stoull(argv[++i]);
        else if (arg == "--k" && i + 1 < argc) k = std::stoi(argv[++i]);
        else if (arg == "--algo" && i + 1 < argc) algo_name = argv[++i];
    }

    std::function<void(std::vector<int>&)> algo_func;
    if (algo_name == "Insertion") algo_func = insertion_sort;
    else if (algo_name == "Merge") algo_func = merge_sort;
    else if (algo_name == "Lomuto") algo_func = quicksort_lomuto;
    else if (algo_name == "Hoare") algo_func = quicksort_hoare;
    else if (algo_name == "3-Way") algo_func = quicksort_3way;
    else if (algo_name == "Counting") algo_func = counting_sort_wrapper;
    else {
        std::cerr << "Unknown algorithm: " << algo_name << "\n";
        return 1;
    }

    if (exp == 1) g_count_k = n;
    else if (exp == 2) g_count_k = n;
    else if (exp == 3) g_count_k = k;

    double total_time = 0;
    for (int t = 0; t < trials; ++t) {
        std::vector<int> data;
        try {
            if (exp == 1) data = generate_exp1_data(n, seed + t);
            else if (exp == 2) data = generate_exp2_data(n, k, seed + t);
            else if (exp == 3) data = generate_exp3_data(n, k, seed + t);
        } catch (const std::bad_alloc& e) {
            std::cerr << "OOM during generation\n";
            return 2;
        }

        std::srand(seed + t);
        
        Timer timer;
        timer.start();
        try {
            algo_func(data);
        } catch (const std::bad_alloc& e) {
            std::cerr << "OOM during sorting\n";
            return 2;
        }
        double elapsed = timer.elapsed_seconds();
        total_time += elapsed;

        verify_sorted(data);
    }
    
    // 輸出 10 次的平均時間到標準輸出
    std::cout << (total_time / trials) << "\n";
    return 0;
}
