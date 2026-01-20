from models import MarketDataPoint, Strategy
from typing import List
from collections import deque

## Strategy1
class NaiveMovingAverageStrategy(Strategy):
    """
    Fixed window = 10
    Space: O(n) because we store full history in self.prices
    Time per tick: O(10) = O(1)
    Total time over n ticks: O(n)
    """

    def __init__(self, window_size: int = 10):
        self.window_size = window_size
        self.prices: List[float] = []

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        self.prices.append(tick.price)

        if len(self.prices) < self.window_size:
            return []

        window = self.prices[-self.window_size:]     # size 10
        avg = sum(window) / self.window_size         # sum 10 values

        if tick.price > avg:
            return ["BUY"]
        elif tick.price < avg:
            return ["SELL"]
        return []

class WindowedMovingAverageStrategy(Strategy):
    """
    Maintains a fixed-size window and updates the average incrementally.

    Time Complexity per tick: O(1)
    Space Complexity: O(k), where k = window size
    """

    def __init__(self, window_size: int):
        self.window_size = window_size
        self.window = deque(maxlen=window_size)
        self.running_sum = 0.0

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        if len(self.window) == self.window_size:
            # Remove the oldest price from the running sum
            self.running_sum -= self.window[0]

        self.window.append(tick.price)
        self.running_sum += tick.price

        if len(self.window) < self.window_size:
            return []

        average_price = self.running_sum / self.window_size

        if tick.price > average_price:
            return ["BUY"]
        elif tick.price < average_price:
            return ["SELL"]
        return []