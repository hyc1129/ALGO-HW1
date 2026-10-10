# 演算法分析 | 排序 程式作業 1 (Sort Benchmark)

這份作業實作了 6 種排序演算法的效能比較，並包含兩個延伸實驗（2b, 3b）。
本專案採用 **C++ (核心排序與測時)** 搭配 **Python (自動化排程與畫圖)** 的混合架構。
C++ 負責精準測時與大陣列記憶體控制；Python 負責捕捉 C++ 程式的崩潰、超時 (5 分鐘限制) 以及產出最終折線圖。

## 1. 開發環境與語言 (Environment & Language)
*   **語言與版本**: 
    *   C++: C++17
    *   Python: Python 3
*   **編譯器**: Microsoft Visual Studio 2022 (MSVC `cl.exe` for x64) / GCC
*   **編譯選項**: `-O2` 或 `/O2` (開啟最佳化)
*   *(詳細的 CPU 型號與實體 RAM (16GB) 等硬體資訊請見 PDF 報告)*

## 2. 編譯指令 (Compilation)
Windows 用戶請在 **x64 Native Tools Command Prompt for VS 2022 (開發人員命令提示字元)** 中執行以下指令，以編譯為 64 位元的執行檔 `sortbench.exe`，避免大陣列時發生 32-bit index overflow 或 out of memory：

```cmd
cl /O2 /EHsc src\*.cpp /Fe:sortbench.exe
```

*(若助教使用 Linux / macOS 或 MinGW 環境，亦可直接使用專案內的 Makefile 編譯：`make`)*

## 3. 重現圖表與數據的指令 (How to reproduce the plots)

本專案將繁瑣的指令參數 (如 `--exp`, `--algo`, `--n`, `--k`, `--trials`, `--seed`) 包裝於 Python 腳本中。
**請務必加上 `-u` 參數執行 Python 避免輸出被緩衝卡住**。

### 3.1 安裝 Python 依賴
```cmd
pip install pandas matplotlib numpy
```

### 3.2 執行實驗以產生 CSV 數據
您可以一次執行全部實驗（時間極長，請耐心等待）：
```cmd
python -u scripts/run_benchmarks.py
```

或者獨立執行各個實驗。每個實驗皆會自動將各條件重複 10 次並取平均。
若單次排序超過 5 分鐘將自動判斷為超時 (Timeout)，遇到 Stack Overflow 則記錄為崩潰 (Crash)：

*   **圖 1 數據 (Experiment 1)**: `python -u scripts/run_benchmarks.py 1`
*   **圖 2 數據 (Experiment 2)**: `python -u scripts/run_benchmarks.py 2`
*   **圖 2b 數據 (Experiment 2b)**: `python -u scripts/run_benchmarks.py 2b`
*   **圖 3 數據 (Experiment 3)**: `python -u scripts/run_benchmarks.py 3`
*   **圖 3b 數據 (Experiment 3b)**: `python -u scripts/run_benchmarks.py 3b`

*(進階說明：Python 內部會獨立啟動 C++ 程式。如果您想手動測試單一設定，C++ 的原始執行指令範例為：`sortbench.exe --exp 1 --algo Merge --n 1024 --k 1024 --trials 1 --seed 0`)*

### 3.3 繪製圖表與計算斜率
當所需的 CSV 檔 (如 `exp1_results.csv`, `exp3_results.csv` 等) 產生完畢後，執行以下指令畫圖：
```cmd
python scripts/plot.py
```
此腳本會：
1. 讀取目前的 CSV 產出對應的 `png` 圖表（雙對數座標 log-log scale）。
2. 對於超時 (Timeout)、記憶體不足 (OOM) 或堆疊溢位崩潰 (Crash) 的點，會在圖表最上方打上 `X` 標記與說明文字，滿足「標示異常點」的作業要求。
3. **在終端機自動印出「實驗一」各演算法的斜率（Global / Early / Late）**，供您直接對照 $O(n^2)$ 與 $O(n \log n)$ 趨勢寫入報告。
