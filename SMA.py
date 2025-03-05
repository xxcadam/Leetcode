from collections import deque
from typing import Optional


class SMA:
    def __init__(self, timespan: int):
        self._timespan = timespan
        self._data = deque()

    def cal(self, new_data: float) -> Optional[float]:
        if len(self._data) == self._timespan:
            self._data.popleft()
        self._data.append(new_data)
        return None if len(self._data) < self._timespan else sum(self._data) / self._timespan

