#include "sorts.hpp"
#include <algorithm>
#include <random>

static std::mt19937_64 g_rng;

void set_sort_seed(uint32_t seed) {
    g_rng.seed(seed);
}

static int64_t get_random_idx(int64_t low, int64_t high) {
    std::uniform_int_distribution<int64_t> dist(low, high);
    return dist(g_rng);
}

// 1. Insertion Sort
void insertion_sort(std::vector<int>& arr) {
    int64_t n = arr.size();
    for (int64_t i = 1; i < n; ++i) {
        int key = arr[i];
        int64_t j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// 2. Merge Sort
void merge(std::vector<int>& arr, std::vector<int>& temp, int64_t left, int64_t mid, int64_t right) {
    int64_t i = left, j = mid + 1, k = left;
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];
    for (i = left; i <= right; ++i) arr[i] = temp[i];
}

void merge_sort_util(std::vector<int>& arr, std::vector<int>& temp, int64_t left, int64_t right) {
    if (left < right) {
        int64_t mid = left + (right - left) / 2;
        merge_sort_util(arr, temp, left, mid);
        merge_sort_util(arr, temp, mid + 1, right);
        merge(arr, temp, left, mid, right);
    }
}

void merge_sort(std::vector<int>& arr) {
    if (arr.empty()) return;
    std::vector<int> temp(arr.size()); // Allocate extra array only once
    merge_sort_util(arr, temp, 0, static_cast<int64_t>(arr.size()) - 1);
}

// 3. Randomized Quicksort (Lomuto partition)
int64_t partition_lomuto(std::vector<int>& arr, int64_t low, int64_t high) {
    // std::rand() on Windows has RAND_MAX=32767. We MUST use 64-bit mt19937_64 to pick valid pivots!
    int64_t pivot_idx = get_random_idx(low, high);
    std::swap(arr[pivot_idx], arr[high]); // Requirement: swap pivot with last element
    int pivot = arr[high];
    int64_t i = low - 1;
    for (int64_t j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quicksort_lomuto_util(std::vector<int>& arr, int64_t low, int64_t high) {
    if (low < high) {
        int64_t pi = partition_lomuto(arr, low, high);
        quicksort_lomuto_util(arr, low, pi - 1);
        quicksort_lomuto_util(arr, pi + 1, high);
    }
}

void quicksort_lomuto(std::vector<int>& arr) {
    if (arr.empty()) return;
    quicksort_lomuto_util(arr, 0, static_cast<int64_t>(arr.size()) - 1);
}

// 3b. Fixed Quicksort (Lomuto partition with fixed last element pivot)
int64_t partition_lomuto_fixed(std::vector<int>& arr, int64_t low, int64_t high) {
    // Fixed pivot at the last element
    int pivot = arr[high];
    int64_t i = low - 1;
    for (int64_t j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quicksort_lomuto_fixed_util(std::vector<int>& arr, int64_t low, int64_t high) {
    if (low < high) {
        int64_t pi = partition_lomuto_fixed(arr, low, high);
        quicksort_lomuto_fixed_util(arr, low, pi - 1);
        quicksort_lomuto_fixed_util(arr, pi + 1, high);
    }
}

void quicksort_lomuto_fixed(std::vector<int>& arr) {
    if (arr.empty()) return;
    quicksort_lomuto_fixed_util(arr, 0, static_cast<int64_t>(arr.size()) - 1);
}

// 4. Randomized Quicksort (Hoare partition)
int64_t partition_hoare(std::vector<int>& arr, int64_t low, int64_t high) {
    int64_t pivot_idx = get_random_idx(low, high);
    int pivot = arr[pivot_idx];
    int64_t i = low - 1;
    int64_t j = high + 1;
    while (true) {
        do { i++; } while (arr[i] < pivot);
        do { j--; } while (arr[j] > pivot);
        if (i >= j) return j;
        std::swap(arr[i], arr[j]);
    }
}

void quicksort_hoare_util(std::vector<int>& arr, int64_t low, int64_t high) {
    if (low < high) {
        int64_t pi = partition_hoare(arr, low, high);
        quicksort_hoare_util(arr, low, pi);
        quicksort_hoare_util(arr, pi + 1, high);
    }
}

void quicksort_hoare(std::vector<int>& arr) {
    if (arr.empty()) return;
    quicksort_hoare_util(arr, 0, static_cast<int64_t>(arr.size()) - 1);
}

// 5. Randomized Quicksort (3-way partition)
void partition_3way(std::vector<int>& arr, int64_t low, int64_t high, int64_t& i, int64_t& j) {
    int64_t pivot_idx = get_random_idx(low, high);
    int pivot = arr[pivot_idx];
    int64_t mid = low;
    i = low;
    j = high;
    while (mid <= j) {
        if (arr[mid] < pivot) {
            std::swap(arr[i], arr[mid]);
            i++;
            mid++;
        } else if (arr[mid] > pivot) {
            std::swap(arr[mid], arr[j]);
            j--;
        } else {
            mid++;
        }
    }
    i = i - 1; // Last element < pivot
    j = j + 1; // First element > pivot
}

void quicksort_3way_util(std::vector<int>& arr, int64_t low, int64_t high) {
    if (low < high) {
        int64_t i, j;
        partition_3way(arr, low, high, i, j);
        quicksort_3way_util(arr, low, i);
        quicksort_3way_util(arr, j, high);
    }
}

void quicksort_3way(std::vector<int>& arr) {
    if (arr.empty()) return;
    quicksort_3way_util(arr, 0, static_cast<int64_t>(arr.size()) - 1);
}

// 6. Counting Sort
void counting_sort(std::vector<int>& arr, int64_t k) {
    if (arr.empty() || k <= 0) return;
    std::vector<int64_t> count(k, 0);
    // Count frequencies
    for (int num : arr) {
        if (num >= 0 && num < k) {
            count[num]++;
        }
    }
    // Write back to original array directly
    int64_t idx = 0;
    for (int64_t i = 0; i < k; ++i) {
        while (count[i] > 0) {
            arr[idx++] = static_cast<int>(i);
            count[i]--;
        }
    }
}
