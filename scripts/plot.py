import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_exp1():
    if not os.path.exists('exp1_results.csv'): return
    df = pd.read_csv('exp1_results.csv')
    
    plt.figure(figsize=(10, 6))
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    
    print("\n--- Experiment 1 Slopes (Δlog2(T) / Δlog2(N)) ---")
    for idx, algo in enumerate(df['Algorithm'].unique()):
        algo_data = df[df['Algorithm'] == algo]
        color = colors[idx % len(colors)]
        
        success_data = algo_data[algo_data['Status'] == 'Success']
        if not success_data.empty:
            plt.plot(success_data['N'], success_data['AverageTime(s)'], marker='o', label=algo, color=color)
            
            # Calculate and print slopes
            if len(success_data) >= 3:
                n_vals = success_data['N'].values
                t_vals = success_data['AverageTime(s)'].values
                
                # Global slope (first to last)
                log_n = np.log2(n_vals)
                log_t = np.log2(t_vals)
                
                global_slope = (log_t[-1] - log_t[0]) / (log_n[-1] - log_n[0])
                
                # Split into early and late to show O(n log n) curve approaching 1
                mid_idx = len(success_data) // 2
                early_slope = (log_t[mid_idx] - log_t[0]) / (log_n[mid_idx] - log_n[0])
                late_slope = (log_t[-1] - log_t[mid_idx]) / (log_n[-1] - log_n[mid_idx])
                
                print(f"[{algo}] Global Slope: {global_slope:.3f} | Early: {early_slope:.3f} -> Late: {late_slope:.3f}")
            
        fail_data = algo_data[algo_data['Status'] != 'Success']
        if not fail_data.empty:
            plt.scatter(fail_data['N'], [300]*len(fail_data), marker='X', color=color, s=100)
            for _, row in fail_data.iterrows():
                plt.text(row['N'], 350, f" {row['Status']}", color=color, rotation=45, va='bottom', fontsize=8)
        
    print("--------------------------------------------------\n")
    plt.xscale('log', base=2)
    plt.yscale('log', base=10)
    plt.xlabel('Array Size N (log2 scale)')
    plt.ylabel('Average Execution Time in seconds (log scale)')
    plt.title('Experiment 1: Time vs Array Size (Uniform Random Data)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.savefig('exp1_plot.png')
    print("Saved exp1_plot.png")

def plot_exp2():
    if not os.path.exists('exp2_results.csv'): return
    df = pd.read_csv('exp2_results.csv')
    
    plt.figure(figsize=(10, 6))
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    for idx, algo in enumerate(df['Algorithm'].unique()):
        algo_data = df[df['Algorithm'] == algo]
        color = colors[idx % len(colors)]
        
        success_data = algo_data[algo_data['Status'] == 'Success']
        if not success_data.empty:
            plt.plot(success_data['K'], success_data['AverageTime(s)'], marker='o', label=algo, color=color)
            
        fail_data = algo_data[algo_data['Status'] != 'Success']
        if not fail_data.empty:
            plt.scatter(fail_data['K'], [300]*len(fail_data), marker='X', color=color, s=100)
            for _, row in fail_data.iterrows():
                plt.text(row['K'], 350, f" {row['Status']}", color=color, rotation=45, va='bottom', fontsize=8)
        
    plt.xscale('log', base=2)
    plt.yscale('log', base=10)
    plt.xlabel('Number of Swaps K (log2 scale)')
    plt.ylabel('Average Execution Time in seconds (log scale)')
    plt.title('Experiment 2: Time vs Swaps K (N=2^20)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.savefig('exp2_plot.png')
    print("Saved exp2_plot.png")

def plot_exp3():
    if not os.path.exists('exp3_results.csv'): return
    df = pd.read_csv('exp3_results.csv')
    
    plt.figure(figsize=(10, 6))
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    for idx, algo in enumerate(df['Algorithm'].unique()):
        algo_data = df[df['Algorithm'] == algo]
        color = colors[idx % len(colors)]
        
        success_data = algo_data[algo_data['Status'] == 'Success']
        if not success_data.empty:
            plt.plot(success_data['K'], success_data['AverageTime(s)'], marker='o', label=algo, color=color)
            
        fail_data = algo_data[algo_data['Status'] != 'Success']
        if not fail_data.empty:
            plt.scatter(fail_data['K'], [300]*len(fail_data), marker='X', color=color, s=100)
            for _, row in fail_data.iterrows():
                plt.text(row['K'], 350, f" {row['Status']}", color=color, rotation=45, va='bottom', fontsize=8)
        
    plt.xscale('log', base=2)
    plt.yscale('log', base=10)
    plt.xlabel('Number of Distinct Values K (log2 scale)')
    plt.ylabel('Average Execution Time in seconds (log scale)')
    plt.title('Experiment 3: Time vs Distinct Values K (N=2^20)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.savefig('exp3_plot.png')
    print("Saved exp3_plot.png")

def plot_exp2b():
    if not os.path.exists('exp2b_results.csv'): return
    df = pd.read_csv('exp2b_results.csv')
    
    plt.figure(figsize=(10, 6))
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    for idx, algo in enumerate(df['Algorithm'].unique()):
        algo_data = df[df['Algorithm'] == algo]
        color = colors[idx % len(colors)]
        
        success_data = algo_data[algo_data['Status'] == 'Success']
        if not success_data.empty:
            plt.plot(success_data['K'], success_data['AverageTime(s)'], marker='o', label=algo, color=color)
            
        fail_data = algo_data[algo_data['Status'] != 'Success']
        if not fail_data.empty:
            plt.scatter(fail_data['K'], [100]*len(fail_data), marker='X', color=color, s=100)
            for _, row in fail_data.iterrows():
                plt.text(row['K'], 120, f" {row['Status']}", color=color, rotation=45, va='bottom', fontsize=8)
        
    plt.xscale('log', base=2)
    plt.yscale('log', base=10)
    plt.xlabel('Number of Swaps K (log2 scale)')
    plt.ylabel('Average Execution Time in seconds (log scale)')
    plt.title('Experiment 2b: Time vs Swaps K (N=2^12)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.savefig('exp2b_plot.png')
    print("Saved exp2b_plot.png")

def plot_exp3b():
    if not os.path.exists('exp3b_results.csv'): return
    df = pd.read_csv('exp3b_results.csv')
    
    plt.figure(figsize=(10, 6))
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    for idx, algo in enumerate(df['Algorithm'].unique()):
        algo_data = df[df['Algorithm'] == algo]
        color = colors[idx % len(colors)]
        
        success_data = algo_data[algo_data['Status'] == 'Success']
        if not success_data.empty:
            plt.plot(success_data['K'], success_data['AverageTime(s)'], marker='o', label=algo, color=color)
            
        fail_data = algo_data[algo_data['Status'] != 'Success']
        if not fail_data.empty:
            plt.scatter(fail_data['K'], [100]*len(fail_data), marker='X', color=color, s=100)
            for _, row in fail_data.iterrows():
                plt.text(row['K'], 120, f" {row['Status']}", color=color, rotation=45, va='bottom', fontsize=8)
        
    plt.xscale('log', base=2)
    plt.yscale('log', base=10)
    plt.xlabel('Number of Distinct Values K (log2 scale)')
    plt.ylabel('Average Execution Time in seconds (log scale)')
    plt.title('Experiment 3b: Time vs Distinct Values K (N=2^12)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.savefig('exp3b_plot.png')
    print("Saved exp3b_plot.png")

if __name__ == '__main__':
    os.makedirs('scripts', exist_ok=True)
    plot_exp1()
    plot_exp2()
    plot_exp3()
    plot_exp2b()
    plot_exp3b()

