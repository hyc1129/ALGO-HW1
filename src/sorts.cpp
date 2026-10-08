#include "sorts.hpp"
#include <cstdlib>
#include <algorithm>

// 1. Insertion Sort
void insertion_sort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// 2. Merge Sort
void merge(std::vector<int>& arr, std::vector<int>& temp, int left, int mid, int right) {
    int i = left, j = mid + 1, k = left;
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];
    for (i = left; i <= right; ++i) arr[i] = temp[i];
}

void merge_sort_util(std::vector<int>& arr, std::vector<int>& temp, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        merge_sort_util(arr, temp, left, mid);
        merge_sort_util(arr, temp, mid + 1, right);
        merge(arr, temp, left, mid, right);
    }
}

void merge_sort(std::vector<int>& arr) {
    if (arr.empty()) return;
    std::vector<int> temp(arr.size()); // Allocate extra array only once
    merge_sort_util(arr, temp, 0, arr.size() - 1);
}

// 3. Randomized Quicksort (Lomuto partition)
int partition_lomuto(std::vector<int>& arr, int low, int high) {
    int pivot_idx = low + std::rand() % (high - low + 1);
    std::swap(arr[pivot_idx], arr[high]); // Requirement: swap pivot with last element
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] <= pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quicksort_lomuto_util(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition_lomuto(arr, low, high);
        quicksort_lomuto_util(arr, low, pi - 1);
        quicksort_lomuto_util(arr, pi + 1, high);
    }
}

void quicksort_lomuto(std::vector<int>& arr) {
    if (arr.empty()) return;
    quicksort_lomuto_util(arr, 0, arr.size() - 1);
}

// 4. Randomized Quicksort (Hoare partition)
int partition_hoare(std::vector<int>& arr, int low, int high) {
    int pivot_idx = low + std::rand() % (high - low + 1);
    int pivot = arr[pivot_idx];
    int i = low - 1;
    int j = high + 1;
    while (true) {
        do { i++; } while (arr[i] < pivot);
        do { j--; } while (arr[j] > pivot);
        if (i >= j) return j;
        std::swap(arr[i], arr[j]);
    }
}

void quicksort_hoare_util(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition_hoare(arr, low, high);
        quicksort_hoare_util(arr, low, pi);
        quicksort_hoare_util(arr, pi + 1, high);
    }
}

void quicksort_hoare(std::vector<int>& arr) {
    if (arr.empty()) return;
    quicksort_hoare_util(arr, 0, arr.size() - 1);
}

// 5. Randomized Quicksort (3-way partition)
void partition_3way(std::vector<int>& arr, int low, int high, int& i, int& j) {
    int pivot_idx = low + std::rand() % (high - low + 1);
    int pivot = arr[pivot_idx];
    int mid = low;
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

void quicksort_3way_util(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int i, j;
        partition_3way(arr, low, high, i, j);
        quicksort_3way_util(arr, low, i);
        quicksort_3way_util(arr, j, high);
    }
}

void quicksort_3way(std::vector<int>& arr) {
    if (arr.empty()) return;
    quicksort_3way_util(arr, 0, arr.size() - 1);
}

// 6. Counting Sort
void counting_sort(std::vector<int>& arr, int k) {
    if (arr.empty() || k <= 0) return;
    std::vector<int> count(k, 0);
    // Count frequencies
    for (int num : arr) {
        if (num >= 0 && num < k) {
            count[num]++;
        }
    }
    // Write back to original array directly
    int idx = 0;
    for (int i = 0; i < k; ++i) {
        while (count[i] > 0) {
            arr[idx++] = i;
            count[i]--;
        }
    }
}

