import subprocess
import csv
import sys
import os

TIMEOUT_SECONDS = 300
ALGOS = ["Insertion", "Merge", "Lomuto", "Hoare", "3-Way", "Counting"]

def get_exe_path():
    if os.path.exists("./sortbench.exe"): return "./sortbench.exe"
    if os.path.exists("./build/Release/sortbench.exe"): return "./build/Release/sortbench.exe"
    return "./sortbench"

def run_cpp(exp, algo, n, k, trials=10, seed=0):
    cmd = [
        get_exe_path(), 
        "--exp", str(exp), 
        "--algo", algo, 
        "--n", str(n), 
        "--k", str(k), 
        "--trials", str(trials), 
        "--seed", str(seed)
    ]
    try:
        # call C++ executable, capture standard output
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT_SECONDS)
        
        if result.returncode == 0:
            return float(result.stdout.strip())
        elif result.returncode == 2:
            print(f"  [OOM] {algo} ran out of memory.")
            return "OOM"
        else:
            print(f"  [Crash] {algo} crashed. Return code: {result.returncode}")
            return "Crash"
    except subprocess.TimeoutExpired:
        print(f"  [Timeout] {algo} exceeded {TIMEOUT_SECONDS}s.")
        return "Timeout"
    except Exception as e:
        print(f"  [Error] {e}")
        return "Error"

def exp1():
    print("=== Starting Experiment 1 ===")
    with open("exp1_results.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Experiment", "N", "K", "Algorithm", "AverageTime(s)"])
        timeout_algos = set()
        
        for p in range(10, 31):
            n = 1 << p
            print(f"Exp 1: N = 2^{p}")
            
            if len(timeout_algos) == len(ALGOS):
                print("All algorithms reached their limits. Stopping Exp 1.")
                break
                
            for algo in ALGOS:
                if algo in timeout_algos: continue
                
                time_taken = run_cpp(1, algo, n, n)
                
                if str(time_taken) in ["Timeout", "OOM", "Crash", "Error"]:
                    timeout_algos.add(algo)
                else:
                    writer.writerow([1, n, n, algo, time_taken])
                    f.flush()
                    print(f"  {algo}: {time_taken:.4f} s")

def exp2():
    print("=== Starting Experiment 2 ===")
    with open("exp2_results.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Experiment", "N", "K", "Algorithm", "AverageTime(s)"])
        timeout_algos = set()
        n = 1 << 20
        
        for p in range(0, 21):
            k = 1 << p
            print(f"Exp 2: N = 2^{20}, K = 2^{p}")
            
            if len(timeout_algos) == len(ALGOS):
                print("All algorithms reached limits. Stopping Exp 2.")
                break
                
            for algo in ALGOS:
                if algo in timeout_algos: continue
                
                time_taken = run_cpp(2, algo, n, k)
                
                if str(time_taken) in ["Timeout", "OOM", "Crash", "Error"]:
                    timeout_algos.add(algo)
                else:
                    writer.writerow([2, n, k, algo, time_taken])
                    f.flush()
                    print(f"  {algo}: {time_taken:.4f} s")

def exp3():
    print("=== Starting Experiment 3 ===")
    with open("exp3_results.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Experiment", "N", "K", "Algorithm", "AverageTime(s)"])
        timeout_algos = set()
        n = 1 << 20
        
        for p in range(0, 21):
            k = 1 << p
            print(f"Exp 3: N = 2^{20}, K = 2^{p}")
            
            if len(timeout_algos) == len(ALGOS):
                print("All algorithms reached limits. Stopping Exp 3.")
                break
                
            for algo in ALGOS:
                if algo in timeout_algos: continue
                
                # Protect Lomuto for small K as per PDF instructions
                if algo == "Lomuto" and k <= 1024:
                    print(f"  [Skipped] {algo} skipped to prevent Stack Overflow.")
                    continue
                    
                time_taken = run_cpp(3, algo, n, k)
                
                if str(time_taken) in ["Timeout", "OOM", "Crash", "Error"]:
                    timeout_algos.add(algo)
                else:
                    writer.writerow([3, n, k, algo, time_taken])
                    f.flush()
                    print(f"  {algo}: {time_taken:.4f} s")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        exp_to_run = int(sys.argv[1])
        if exp_to_run == 1: exp1()
        elif exp_to_run == 2: exp2()
        elif exp_to_run == 3: exp3()
        else: print(f"Unknown experiment: {exp_to_run}")
    else:
        exp1()
        exp2()
        exp3()
