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
    times = []
    for t in range(trials):
        cmd = [
            get_exe_path(), 
            "--exp", str(exp), 
            "--algo", algo, 
            "--n", str(n), 
            "--k", str(k), 
            "--trials", "1", 
            "--seed", str(seed + t)
        ]
        try:
            # call C++ executable, capture standard output
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT_SECONDS)
            
            if result.returncode == 0:
                out_str = result.stdout.strip()
                
                # Anaconda Windows bug workaround: Read from file if stdout is missing or unparseable
                if os.path.exists(".result.txt"):
                    with open(".result.txt", "r") as f:
                        file_out = f.read().strip()
                    os.remove(".result.txt")
                    if file_out:
                        out_str = file_out

                try:
                    lines = out_str.split('\n')
                    times.append(float(lines[-1].strip()))
                except ValueError:
                    print(f"  [Error] Failed to parse output: {repr(out_str)}", flush=True)
                    print(f"  [Action Required] Please RECOMPILE the C++ program! The executable is out of date.", flush=True)
                    return "Error", times
            elif result.returncode == 2:
                print(f"  [OOM] {algo} ran out of memory.", flush=True)
                return "OOM", times
            else:
                print(f"  [Crash] {algo} crashed. Return code: {result.returncode}", flush=True)
                return "Crash", times
        except subprocess.TimeoutExpired:
            print(f"  [Timeout] {algo} exceeded {TIMEOUT_SECONDS}s on trial {t+1}.", flush=True)
            return "Timeout", times
        except Exception as e:
            print(f"  [Error] {e}", flush=True)
            return "Error", times
    
    return sum(times) / trials, times

def exp1():
    print("=== Starting Experiment 1 ===")
    with open("exp1_results.csv", "w", newline='') as f:
        writer = csv.writer(f)
        headers = ["Experiment", "N", "K", "Algorithm", "AverageTime(s)", "Status"] + [f"Trial{i+1}(s)" for i in range(10)]
        writer.writerow(headers)
        timeout_algos = set()
        
        for p in range(10, 31):
            n = 1 << p
            print(f"Exp 1: N = 2^{p}")
            
            if len(timeout_algos) == len(ALGOS):
                print("All algorithms reached their limits. Stopping Exp 1.")
                break
                
            for algo in ALGOS:
                if algo in timeout_algos: continue
                
                time_taken, times = run_cpp(1, algo, n, n)
                
                times_str = [f"{t:.6f}" for t in times]
                while len(times_str) < 10:
                    times_str.append("")
                
                if str(time_taken) in ["Timeout", "OOM", "Crash", "Error"]:
                    writer.writerow([1, n, n, algo, "", str(time_taken)] + times_str)
                    if str(time_taken) in ["Timeout", "OOM"]:
                        timeout_algos.add(algo)
                else:
                    writer.writerow([1, n, n, algo, time_taken, "Success"] + times_str)
                    print(f"  {algo}: {time_taken:.4f} s")
                f.flush()

def exp2():
    print("=== Starting Experiment 2 ===")
    with open("exp2_results.csv", "w", newline='') as f:
        writer = csv.writer(f)
        headers = ["Experiment", "N", "K", "Algorithm", "AverageTime(s)", "Status"] + [f"Trial{i+1}(s)" for i in range(10)]
        writer.writerow(headers)
        timeout_algos = set()
        n = 1 << 18
        
        for p in range(0, 21):
            k = 1 << p
            print(f"Exp 2: N = 2^{18}, K = 2^{p}")
            
            if len(timeout_algos) == len(ALGOS):
                print("All algorithms reached limits. Stopping Exp 2.")
                break
                
            for algo in ALGOS:
                if algo in timeout_algos: continue
                
                time_taken, times = run_cpp(2, algo, n, k)
                
                times_str = [f"{t:.6f}" for t in times]
                while len(times_str) < 10:
                    times_str.append("")
                
                if str(time_taken) in ["Timeout", "OOM", "Crash", "Error"]:
                    writer.writerow([2, n, k, algo, "", str(time_taken)] + times_str)
                    if str(time_taken) in ["Timeout", "OOM"]:
                        timeout_algos.add(algo)
                else:
                    writer.writerow([2, n, k, algo, time_taken, "Success"] + times_str)
                    print(f"  {algo}: {time_taken:.4f} s")
                f.flush()

def exp3():
    print("=== Starting Experiment 3 ===")
    with open("exp3_results.csv", "w", newline='') as f:
        writer = csv.writer(f)
        headers = ["Experiment", "N", "K", "Algorithm", "AverageTime(s)", "Status"] + [f"Trial{i+1}(s)" for i in range(10)]
        writer.writerow(headers)
        timeout_algos = set()
        n = 1 << 18
        
        for p in range(0, 21):
            k = 1 << p
            print(f"Exp 3: N = 2^{18}, K = 2^{p}")
            
            if len(timeout_algos) == len(ALGOS):
                print("All algorithms reached limits. Stopping Exp 3.")
                break
                
            for algo in ALGOS:
                if algo in timeout_algos: continue
                
                time_taken, times = run_cpp(3, algo, n, k)
                
                times_str = [f"{t:.6f}" for t in times]
                while len(times_str) < 10:
                    times_str.append("")
                
                if str(time_taken) in ["Timeout", "OOM", "Crash", "Error"]:
                    writer.writerow([3, n, k, algo, "", str(time_taken)] + times_str)
                    if str(time_taken) in ["Timeout", "OOM"]:
                        timeout_algos.add(algo)
                else:
                    writer.writerow([3, n, k, algo, time_taken, "Success"] + times_str)
                    print(f"  {algo}: {time_taken:.4f} s")
                f.flush()

def exp2b():
    print("=== Starting Experiment 2b ===")
    with open("exp2b_results.csv", "w", newline='') as f:
        writer = csv.writer(f)
        headers = ["Experiment", "N", "K", "Algorithm", "AverageTime(s)", "Status"] + [f"Trial{i+1}(s)" for i in range(10)]
        writer.writerow(headers)
        
        algos_2b = ["Lomuto", "Lomuto-Fixed"]
        timeout_algos = set()
        n = 1 << 12
        
        for p in range(0, 13):
            k = 1 << p
            print(f"Exp 2b: N = 2^{12}, K = 2^{p}")
            
            for algo in algos_2b:
                if algo in timeout_algos: continue
                time_taken, times = run_cpp(2, algo, n, k)
                
                times_str = [f"{t:.6f}" for t in times]
                while len(times_str) < 10:
                    times_str.append("")
                
                if str(time_taken) in ["Timeout", "OOM", "Crash", "Error"]:
                    writer.writerow(["2b", n, k, algo, "", str(time_taken)] + times_str)
                    if str(time_taken) in ["Timeout", "OOM"]:
                        timeout_algos.add(algo)
                else:
                    writer.writerow(["2b", n, k, algo, time_taken, "Success"] + times_str)
                    print(f"  {algo}: {time_taken:.4f} s")
                f.flush()

def exp3b():
    print("=== Starting Experiment 3b ===")
    with open("exp3b_results.csv", "w", newline='') as f:
        writer = csv.writer(f)
        headers = ["Experiment", "N", "K", "Algorithm", "AverageTime(s)", "Status"] + [f"Trial{i+1}(s)" for i in range(10)]
        writer.writerow(headers)
        
        timeout_algos = set()
        n = 1 << 12
        
        for p in range(0, 13):
            k = 1 << p
            print(f"Exp 3b: N = 2^{12}, K = 2^{p}")
            
            for algo in ALGOS:
                if algo in timeout_algos: continue
                time_taken, times = run_cpp(3, algo, n, k)
                
                times_str = [f"{t:.6f}" for t in times]
                while len(times_str) < 10:
                    times_str.append("")
                
                if str(time_taken) in ["Timeout", "OOM", "Crash", "Error"]:
                    writer.writerow(["3b", n, k, algo, "", str(time_taken)] + times_str)
                    if str(time_taken) in ["Timeout", "OOM"]:
                        timeout_algos.add(algo)
                else:
                    writer.writerow(["3b", n, k, algo, time_taken, "Success"] + times_str)
                    print(f"  {algo}: {time_taken:.4f} s")
                f.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        exp_to_run = sys.argv[1]
        if exp_to_run == "1": exp1()
        elif exp_to_run == "2": exp2()
        elif exp_to_run == "3": exp3()
        elif exp_to_run == "2b": exp2b()
        elif exp_to_run == "3b": exp3b()
        else: print(f"Unknown experiment: {exp_to_run}")
    else:
        exp1()
        exp2()
        exp2b()
        exp3()
        exp3b()
