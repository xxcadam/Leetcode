from collections import deque


class EMA:
    def __init__(self, timespan: int, ema_span: int = 5):
        self._timespan = timespan
        self._data = deque()
        self._ema_span = ema_span
        self._ema = EMA(ema_span)

    def cal(self, new_data: float):
        if len(self._data) < self._ema_span:
            self._ema.cal(new_data)
        else:
            pass

