#include "sorts.hpp"
#include "generators.hpp"
#include "utils.hpp"
#include <iostream>
#include <vector>
#include <string>
#include <functional>
#include <fstream>
#include <cstdlib>

struct Algorithm {
    std::string name;
    std::function<void(std::vector<int>&)> func;
    bool timeout;
};

int g_count_k = 0;
void counting_sort_wrapper(std::vector<int>& arr) {
    counting_sort(arr, g_count_k);
}

void run_experiment(int exp, int trials, int start_seed) {
    std::vector<Algorithm> algos = {
        {"Insertion", insertion_sort, false},
        {"Merge", merge_sort, false},
        {"Lomuto", quicksort_lomuto, false},
        {"Hoare", quicksort_hoare, false},
        {"3-Way", quicksort_3way, false},
        {"Counting", counting_sort_wrapper, false}
    };

    std::ofstream out("exp" + std::to_string(exp) + "_results.csv");
    out << "Experiment,N,K,Algorithm,AverageTime(s)\n";

    if (exp == 1) {
        // Exp 1: N from 2^10 to 2^30
        for (int p = 10; p <= 30; ++p) {
            size_t n = 1ULL << p;
            g_count_k = n; // For Exp 1, values are 0 to n-1
            std::cout << "\n[Exp 1] Running N = 2^" << p << std::endl;

            for (auto& algo : algos) {
                if (algo.timeout) continue;
                
                double total_time = 0;
                bool skipped = false;

                for (int t = 0; t < trials; ++t) {
                    std::vector<int> data = generate_exp1_data(n, start_seed + t);
                    std::srand(start_seed + t); // Set seed for quicksort pivots
                    
                    Timer timer;
                    timer.start();
                    algo.func(data);
                    double elapsed = timer.elapsed_seconds();
                    total_time += elapsed;

                    verify_sorted(data);

                    if (elapsed > 300.0) { // 5 minutes limit
                        algo.timeout = true;
                        std::cout << "  " << algo.name << " Timeout (>5m). Stopping for larger N.\n";
                        break;
                    }
                }
                if (!algo.timeout && !skipped) {
                    double avg = total_time / trials;
                    std::cout << "  " << algo.name << ": " << avg << " s\n";
                    out << "1," << n << "," << n << "," << algo.name << "," << avg << "\n";
                }
            }
        }
    } else if (exp == 2) {
        // Exp 2: N = 2^20 (or smaller if needed, but instructions say 2^20). K from 2^0 to 2^20.
        size_t n = 1ULL << 20;
        g_count_k = n;
        for (int p = 0; p <= 20; ++p) {
            int k = 1 << p;
            std::cout << "\n[Exp 2] Running N = 2^20, K = 2^" << p << std::endl;

            for (auto& algo : algos) {
                if (algo.timeout) continue;
                
                double total_time = 0;
                for (int t = 0; t < trials; ++t) {
                    std::vector<int> data = generate_exp2_data(n, k, start_seed + t);
                    std::srand(start_seed + t);
                    
                    Timer timer;
                    timer.start();
                    algo.func(data);
                    double elapsed = timer.elapsed_seconds();
                    total_time += elapsed;

                    verify_sorted(data);

                    if (elapsed > 300.0) {
                        algo.timeout = true;
                        std::cout << "  " << algo.name << " Timeout (>5m). Stopping for larger K.\n";
                        break;
                    }
                }
                if (!algo.timeout) {
                    double avg = total_time / trials;
                    std::cout << "  " << algo.name << ": " << avg << " s\n";
                    out << "2," << n << "," << k << "," << algo.name << "," << avg << "\n";
                }
            }
        }
    } else if (exp == 3) {
        // Exp 3: N = 2^20, K from 2^0 to 2^20
        size_t n = 1ULL << 20;
        for (int p = 0; p <= 20; ++p) {
            int k = 1 << p;
            g_count_k = k;
            std::cout << "\n[Exp 3] Running N = 2^20, K = 2^" << p << std::endl;

            for (auto& algo : algos) {
                if (algo.timeout) continue;

                // Protect against Lomuto stack overflow for small K
                if (algo.name == "Lomuto" && k <= 1024) {
                    std::cout << "  " << algo.name << " skipped for K <= 1024 to prevent Stack Overflow.\n";
                    continue;
                }

                double total_time = 0;
                for (int t = 0; t < trials; ++t) {
                    std::vector<int> data = generate_exp3_data(n, k, start_seed + t);
                    std::srand(start_seed + t);
                    
                    Timer timer;
                    timer.start();
                    algo.func(data);
                    double elapsed = timer.elapsed_seconds();
                    total_time += elapsed;

                    verify_sorted(data);

                    if (elapsed > 300.0) {
                        algo.timeout = true;
                        std::cout << "  " << algo.name << " Timeout (>5m). Stopping for larger K.\n";
                        break;
                    }
                }
                if (!algo.timeout && !(algo.name == "Lomuto" && k <= 1024)) {
                    double avg = total_time / trials;
                    std::cout << "  " << algo.name << ": " << avg << " s\n";
                    out << "3," << n << "," << k << "," << algo.name << "," << avg << "\n";
                }
            }
        }
    }
}

int main(int argc, char* argv[]) {
    int exp = 1;
    int trials = 10;
    int seed = 0;

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--exp" && i + 1 < argc) {
            exp = std::stoi(argv[++i]);
        } else if (arg == "--trials" && i + 1 < argc) {
            trials = std::stoi(argv[++i]);
        } else if (arg == "--seed" && i + 1 < argc) {
            seed = std::stoi(argv[++i]);
        }
    }

    std::cout << "Starting Experiment " << exp << " with " << trials << " trials, seed " << seed << std::endl;
    run_experiment(exp, trials, seed);

    return 0;
}
