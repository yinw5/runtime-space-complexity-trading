# Runtime & Space Complexity in Financial Signal Processing

## Overview
This project analyzes the runtime and space complexity of moving average trading strategies on market data.

## Setup

Install dependencies:

pip install memory-profiler matplotlib

## How to Run

python main.py

This will:
- Load market data
- Benchmark both strategies
- Generate plots
- Save results to PNG files

## File Structure

data_loader.py      - CSV parsing and dataclass creation
strategies.py       - Naive and windowed strategies
profiler.py         - Runtime and memory measurement  
reporting.py        - Plot generation helpers
main.py             - Runs the full experiment
complexity_report.md - Detailed analysis report

## Output

- runtime_vs_input_size.png
- memory_vs_input_size.png 
