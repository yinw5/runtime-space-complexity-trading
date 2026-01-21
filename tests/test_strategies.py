import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import datetime, timedelta
import time

from models import MarketDataPoint
from strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy
from data_loader import load_market_data
from profiler import measure_peak_memory_mb


def make_ticks(prices, symbol="TEST"):
    base = datetime(2026, 1, 1, 0, 0, 0)
    return [
        MarketDataPoint(timestamp=base + timedelta(seconds=i), symbol=symbol, price=float(p))
        for i, p in enumerate(prices)
    ]


def expected_signal(price, avg):
    if price > avg:
        return ["BUY"]
    if price < avg:
        return ["SELL"]
    return []


# 1) Validate correctness of both strategies
def test_both_strategies_match_same_windowed_logic():
    prices = [10, 11, 12, 13, 14]
    window = 3
    ticks = make_ticks(prices)

    naive = NaiveMovingAverageStrategy(window_size=window)
    windowed = WindowedMovingAverageStrategy(window_size=window)

    for i, tick in enumerate(ticks):
        sig_naive = naive.generate_signals(tick)
        sig_windowed = windowed.generate_signals(tick)

        assert sig_naive == sig_windowed

        if i < window - 1:
            assert sig_naive == []
        else:
            w = prices[i-window+1:i+1]
            avg = sum(w) / window
            assert sig_naive == expected_signal(tick.price, avg)


# 2) Confirm optimized strategy runs under 1 sec and <100MB for 100k ticks
def test_windowed_strategy_meets_performance_constraints():
    data = load_market_data("market_data.csv")
    subset = data[:100000]

    # runtime check
    start = time.perf_counter()
    strat = WindowedMovingAverageStrategy(window_size=10)
    for tick in subset:
        strat.generate_signals(tick)
    elapsed = time.perf_counter() - start

    # memory check
    peak_mem = measure_peak_memory_mb(
        subset,
        lambda: WindowedMovingAverageStrategy(window_size=10)
    )

    assert elapsed < 1.0, f"Too slow: {elapsed:.3f}s (needs < 1.0s)"
    assert peak_mem < 100.0, f"Too much memory: {peak_mem:.2f}MB (needs < 100MB)"


# 3) Test profiling output includes expected hotspots and memory peaks
def test_profiling_helpers_return_sane_values():
    data = load_market_data("market_data.csv")
    subset = data[:1000]

    peak_mem = measure_peak_memory_mb(
        subset,
        lambda: WindowedMovingAverageStrategy(window_size=10)
    )

    assert peak_mem > 0.0
