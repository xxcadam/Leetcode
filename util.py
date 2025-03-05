from datetime import datetime


def is_4hour_specific(time: datetime):
    SPECIFIC_HOURS = [0, 4, 8, 12, 16, 20]
    return time.hour in SPECIFIC_HOURS and time.minute == 0 and time.second == 0 and time.microsecond == 0
