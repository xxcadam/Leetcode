from typing import Optional, List

from trader.Algo import Algo
from trader.Candle import Candle
from trader.EMA import EMA
from trader.SMA import SMA
from trader.strategy import Strategy
from trader.util import is_4hour_specific


class Broker:

    def __init__(self):
        self._iter_data: Optional[List[Candle]] = None
        self._iter_data_unit: Optional[str] = None
        self._strategy: Optional[Strategy] = None
        self._4hourData: Optional[List[Candle]] = None
        self._tracking_lines = {}
        # self._15minData: Optional[List[Candle]] = None

    def load_data(self, unit) -> None:
        self._iter_data = []
        self._iter_data_unit = unit

    def add_strategy(self, strategy: Strategy):
        self._strategy = strategy
        strategy.setBroker(self)

    def start(self):
        candle_4hr = None
        for row in self._iter_data:
            if candle_4hr is None:
                candle_4hr = Candle(
                    gmt_time=row.gmt_time,
                    open=row.open,
                    close=row.close,
                    high=row.high,
                    low=row.low,
                    volume=row.volume
                )
            else:
                candle_4hr.high = max(row.high, candle_4hr.high)
                candle_4hr.low = min(row.low, candle_4hr.low)
                candle_4hr.volume += row.volume
                if is_4hour_specific(row.gmt_time):
                    candle_4hr.gmt_time = row.gmt_time
                    candle_4hr.close = row.close
                    self._4hourData.append(candle_4hr)
                    candle_4hr = None

            self._strategy.tick(row)

    def get_last_4hour_candle(self) -> Candle:
        return self._4hourData[-1]

    def get_4hour_data(self) -> List[Candle]:
        return self._4hourData

    def customize_line(self, algo: Algo, timespan: int) -> None:
        name = f'{algo.value}_{timespan}'
        if name in self._tracking_lines.keys():
            print(f'name is already tracked, continue')
        self._tracking_lines[name] = EMA(timespan) if algo == Algo.EMA else SMA(timespan)







