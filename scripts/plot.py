import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_exp1():
    if not os.path.exists('exp1_results.csv'): return
    df = pd.read_csv('exp1_results.csv')
    
    plt.figure(figsize=(10, 6))
    for algo in df['Algorithm'].unique():
        algo_data = df[df['Algorithm'] == algo]
        plt.plot(algo_data['N'], algo_data['AverageTime(s)'], marker='o', label=algo)
        
    plt.xscale('log', base=2)
    plt.yscale('log', base=10)
    plt.xlabel('Array Size N (log2 scale)')
    plt.ylabel('Average Execution Time in seconds (log scale)')
    plt.title('Experiment 1: Time vs Array Size (Uniform Random Data)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig('exp1_plot.png')
    print("Saved exp1_plot.png")

def plot_exp2():
    if not os.path.exists('exp2_results.csv'): return
    df = pd.read_csv('exp2_results.csv')
    
    plt.figure(figsize=(10, 6))
    for algo in df['Algorithm'].unique():
        algo_data = df[df['Algorithm'] == algo]
        plt.plot(algo_data['K'], algo_data['AverageTime(s)'], marker='o', label=algo)
        
    plt.xscale('log', base=2)
    plt.yscale('log', base=10)
    plt.xlabel('Number of Swaps K (log2 scale)')
    plt.ylabel('Average Execution Time in seconds (log scale)')
    plt.title('Experiment 2: Time vs Swaps K (N=2^20)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig('exp2_plot.png')
    print("Saved exp2_plot.png")

def plot_exp3():
    if not os.path.exists('exp3_results.csv'): return
    df = pd.read_csv('exp3_results.csv')
    
    plt.figure(figsize=(10, 6))
    for algo in df['Algorithm'].unique():
        algo_data = df[df['Algorithm'] == algo]
        plt.plot(algo_data['K'], algo_data['AverageTime(s)'], marker='o', label=algo)
        
    plt.xscale('log', base=2)
    plt.yscale('log', base=10)
    plt.xlabel('Number of Distinct Values K (log2 scale)')
    plt.ylabel('Average Execution Time in seconds (log scale)')
    plt.title('Experiment 3: Time vs Distinct Values K (N=2^20)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig('exp3_plot.png')
    print("Saved exp3_plot.png")

if __name__ == '__main__':
    # create scripts dir if it doesn't exist
    os.makedirs('scripts', exist_ok=True)
    plot_exp1()
    plot_exp2()
    plot_exp3()
