from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class MarketDataPoint:
    timestamp: datetime
    symbol: str
    price: float


class Strategy(ABC): #ABC = Abstract Base Class = this is not meant to be used directly but for defining rules for subclasses
    @abstractmethod
    def generate_signals(self, tick: MarketDataPoint) -> list: #RULE = every subclass MUST implement generate_signals that takes MArketDataPint and return a list

        pass

# Overall, this ABC allows us to compare and profile multiple strategies fairly, because they all run in the same pipeline and implement the same generate_signals interface
