from typing import Optional

from trader.Broker import Broker
from trader.Candle import Candle
from trader.util import is_4hour_specific


class Strategy:
    def __init__(self):
        self._broker: Optional[Broker] = None

    def setBroker(self, broker: Broker):
        self._broker = broker

    def tick(self, data: Candle):
        if is_4hour_specific(data.gmt_time):
            candle_4hr = self._broker.get_last_4hour_candle()
