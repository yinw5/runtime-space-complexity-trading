import csv
from datetime import datetime
from models import MarketDataPoint
from typing import List

def load_market_data(path: str) -> List[MarketDataPoint]:

    data_points: List[MarketDataPoint] = []

    with open(path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            timestamp = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")

            market_datapoint = MarketDataPoint(
                timestamp=timestamp,
                symbol=row[1],
                price=float(row[2])
            )

            data_points.append(market_datapoint)

    data_points.sort(key=lambda p: p.timestamp)

    return data_points

# space complexity Big-O analysis:
#   for n rows, this requires O(n) space to store the full dataset in memory since memory usage grows linearly with the number of ticks.