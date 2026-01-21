from models import MarketDataPoint, Strategy
from typing import List, Callable
import timeit
from memory_profiler import memory_usage

def run_strategy(data: List[MarketDataPoint], strategy: Strategy) -> None:
    for tick in data:
        strategy.generate_signals(tick)


def measure_time(
    data: List[MarketDataPoint],
    make_strategy: Callable[[], Strategy]
) -> float:
    
    def _task():
        strategy = make_strategy()
        for tick in data:
            strategy.generate_signals(tick)

    t = timeit.timeit(_task, number=1)
    return t


def measure_peak_memory(
    data: List[MarketDataPoint],
    make_strategy: Callable[[], Strategy],
) -> float:

    def _task():
        strategy = make_strategy()
        for tick in data:
            strategy.generate_signals(tick)

    samples_mb = memory_usage((_task,), interval=0.01)
    return max(samples_mb)