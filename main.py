from data_loader import load_market_data
from strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy
from profiler import measure_time_timeit, measure_peak_memory_mb

import matplotlib.pyplot as plt

def main():
    data = load_market_data("market_data.csv")
    sizes = [1000, 10000, 100000]

    # Store results for plotting
    naive_times = []
    windowed_times = []

    naive_memory = []
    windowed_memory = []

    for n in sizes:
        subset = data[:n]

        # Runtime (timeit) — use fresh strategy each time
        t_naive = measure_time_timeit(subset, lambda: NaiveMovingAverageStrategy())
        t_windowed = measure_time_timeit(subset, lambda: WindowedMovingAverageStrategy(window_size=10))

        # Peak memory
        m_naive = measure_peak_memory_mb(subset, lambda: NaiveMovingAverageStrategy())
        m_windowed = measure_peak_memory_mb(subset, lambda: WindowedMovingAverageStrategy(window_size=10))

        # Save results
        naive_times.append(t_naive)
        windowed_times.append(t_windowed)

        naive_memory.append(m_naive)
        windowed_memory.append(m_windowed)

        print(f"{n} ticks:")
        print(f"  Naive time:     {t_naive:.6f} s | peak mem: {m_naive:.2f} MB")
        print(f"  Windowed time:  {t_windowed:.6f} s | peak mem: {m_windowed:.2f} MB")
        print()

    # -------- Plot 1: Runtime vs Input Size --------
    plt.figure(figsize=(6, 4))
    plt.plot(sizes, naive_times, marker="o", label="Naive")
    plt.plot(sizes, windowed_times, marker="o", label="Windowed")

    plt.xlabel("Number of ticks (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime vs Input Size")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("runtime_vs_input_size.png")

    # -------- Plot 2: Memory vs Input Size --------
    plt.figure(figsize=(6, 4))
    plt.plot(sizes, naive_memory, marker="o", label="Naive")
    plt.plot(sizes, windowed_memory, marker="o", label="Windowed")

    plt.xlabel("Number of ticks (n)")
    plt.ylabel("Peak Memory (MB)")
    plt.title("Memory Usage vs Input Size")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("memory_vs_input_size.png")
    plt.show()


if __name__ == "__main__":
    main()
