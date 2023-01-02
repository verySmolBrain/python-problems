from collections import defaultdict
from bisect import bisect

class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''