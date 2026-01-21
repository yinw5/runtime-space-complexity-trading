from data_loader import load_market_data
from strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy
from profiler import measure_time, measure_peak_memory
from reporting import runtime_plot, memory_plot

def main():
    data = load_market_data("market_data.csv")
    sizes = [1000, 10000, 100000]

    naive_times = []
    windowed_times = []

    naive_memory = []
    windowed_memory = []

    for n in sizes:
        subset = data[:n]

        # timeit
        t_naive = measure_time(subset, lambda: NaiveMovingAverageStrategy())
        t_windowed = measure_time(subset, lambda: WindowedMovingAverageStrategy(window_size=10))

        # peak memory
        m_naive = measure_peak_memory(subset, lambda: NaiveMovingAverageStrategy())
        m_windowed = measure_peak_memory(subset, lambda: WindowedMovingAverageStrategy(window_size=10))

        naive_times.append(t_naive)
        windowed_times.append(t_windowed)

        naive_memory.append(m_naive)
        windowed_memory.append(m_windowed)

        print(f"{n} ticks:")
        print(f"  Naive time:     {t_naive:.6f} s | peak mem: {m_naive:.2f} MB")
        print(f"  Windowed time:  {t_windowed:.6f} s | peak mem: {m_windowed:.2f} MB")
        print()

    runtime_plot(sizes, naive_times, windowed_times)
    memory_plot(sizes, naive_memory, windowed_memory)


if __name__ == "__main__":
    main()

