# Sort Benchmark Project

This project implements and benchmarks 6 sorting algorithms as required by the assignment.

## Directory Structure
- `src/`: C++ source code.
- `scripts/`: Python scripts for plotting.
- `Makefile`: For Linux/Mac/MinGW (TA grading).
- `CMakeLists.txt`: For modern IDE integration (Windows/Cross-platform).

## Compilation
You can compile using `make` (preferred for grading):
```bash
make
```

Or using CMake:
```bash
cmake -B build
cmake --build build --config Release
```

## Running Experiments
The executable `sortbench` takes three arguments: `--exp`, `--trials`, and `--seed`.

**Experiment 1: Random array (N=2^10 to 2^30)**
```bash
./sortbench --exp 1 --trials 10 --seed 0
```
This generates `exp1_results.csv`.

**Experiment 2: Nearly sorted array (N=2^20, K random swaps)**
```bash
./sortbench --exp 2 --trials 10 --seed 0
```
This generates `exp2_results.csv`.

**Experiment 3: Array with many duplicates (N=2^20, K distinct values)**
```bash
./sortbench --exp 3 --trials 10 --seed 0
```
This generates `exp3_results.csv`.

*Note: In Exp 3, Lomuto partition will stack overflow for small K. To prevent the entire script from crashing and losing data, the code intentionally skips Lomuto for K <= 1024.*

## Plotting
Requires Python 3, `pandas`, and `matplotlib`.
```bash
python scripts/plot.py
```
This script reads the CSV files and generates the required log-log plots.
