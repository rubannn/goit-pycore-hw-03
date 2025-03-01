"""
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
"""

# import datetime as dt
from datetime import datetime


def get_days_from_today(date):
    date_format = "%Y-%m-%d"
    xday = datetime.strptime(date, date_format)
    today = datetime.today()
    return (today - xday).days


tests = ["2020-10-09", "2025-12-12"]

for i, dt in enumerate(tests):
    print(f"test[{i}] -> {get_days_from_today(dt)}")
