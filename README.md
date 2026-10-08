# Sort Benchmark Project

This project implements and benchmarks 6 sorting algorithms. It uses a **Python Orchestrator + C++ Worker** architecture to guarantee that if an algorithm crashes (e.g., Out of Memory or Stack Overflow), it gracefully skips and continues without stopping the entire experiment.

## Directory Structure
- `src/`: C++ source code.
- `scripts/`: Python scripts for orchestration and plotting.
- `Makefile` & `CMakeLists.txt`: Build configurations.

## Compilation
You can compile using `make` (preferred for Linux/MinGW grading):
```bash
make
```

Or using CMake (for IDEs):
```bash
cmake -B build
cmake --build build --config Release
```

## Running Experiments
Use the Python orchestrator script to run the benchmarks safely. 

**Run ALL experiments sequentially:**
```bash
python scripts/run_benchmarks.py
```

**Run independently (e.g., only Experiment 1):**
```bash
python scripts/run_benchmarks.py 1
python scripts/run_benchmarks.py 2
python scripts/run_benchmarks.py 3
```

*(Note: The orchestrator handles the 5-minute timeout and any unexpected crashes (like OOM). It also skips Lomuto for Exp 3 when K <= 1024 to prevent Stack Overflows as instructed.)*

## Plotting
Requires Python 3, `pandas`, and `matplotlib`.
```bash
python scripts/plot.py
```
This script reads the CSV files and generates the required log-log plots.
