import random
from datetime import date


def generate_date(year=None, month=None, day=None) -> date:
    if year is None:
        year = random.randint(2000, 2025)
    if month is None:
        month = random.randint(1, 12)
    if day is None:
        if month in [4, 6, 9, 11]:
            day = random.randint(1, 30)
        elif month == 2:
            day = random.randint(1, 28)  # Ignoring leap years for simplicity
        else:
            day = random.randint(1, 31)
    return date(year, month, day)