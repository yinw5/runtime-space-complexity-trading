import matplotlib.pyplot as plt

def runtime_plot(sizes, naive_times, windowed_times, filename="runtime_vs_input_size.png"):
    plt.figure(figsize=(6, 4))
    plt.plot(sizes, naive_times, marker="o", label="Naive")
    plt.plot(sizes, windowed_times, marker="o", label="Windowed")
    plt.xlabel("Number of ticks (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime vs Input Size")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def memory_plot(sizes, naive_memory, windowed_memory, filename="memory_vs_input_size.png"):
    plt.figure(figsize=(6, 4))
    plt.plot(sizes, naive_memory, marker="o", label="Naive")
    plt.plot(sizes, windowed_memory, marker="o", label="Windowed")
    plt.xlabel("Number of ticks (n)")
    plt.ylabel("Peak Memory (MB)")
    plt.title("Memory Usage vs Input Size")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

