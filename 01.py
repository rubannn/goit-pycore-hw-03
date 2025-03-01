"""
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
"""

# import datetime as dt
from datetime import datetime


def get_days_from_today(date: str) -> int:
    date_format = "%Y-%m-%d"
    today = datetime.today()
    try:
        xday = datetime.strptime(date, date_format)
    except Exception as e:
        return f"{type(e)}: {e}"
    return (today - xday).days


tests = ["2020-10-09", "2025-12-12", "2021-13-13", "2021-10-09"]

for i, dt in enumerate(tests):
    print(f"[{i}] {dt} \t->\t {get_days_from_today(dt)}")
