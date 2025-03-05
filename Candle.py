from dataclasses import dataclass
from datetime import datetime


@dataclass
class Candle:
    gmt_time: datetime
    open: float
    close: float
    high: float
    low: float
    volume: float
