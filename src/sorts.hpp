#ifndef SORTS_HPP
#define SORTS_HPP

#include <vector>
#include <cstdint>

void set_sort_seed(uint32_t seed);

void insertion_sort(std::vector<int>& arr);
void merge_sort(std::vector<int>& arr);
void quicksort_lomuto(std::vector<int>& arr);
void quicksort_lomuto_fixed(std::vector<int>& arr);
void quicksort_hoare(std::vector<int>& arr);
void quicksort_3way(std::vector<int>& arr);
void counting_sort(std::vector<int>& arr, int64_t k);

#endif // SORTS_HPP
