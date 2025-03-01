"""
У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження.
Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе
вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого
день народження вперед на 7 днів включаючи поточний день.

У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я
користувача та його день народження. Оскільки дні народження колег можуть припадати
на вихідні, ваша функція також повинна враховувати це та переносити дату привітання
на наступний робочий день, якщо необхідно.
"""

from datetime import datetime, date


def get_upcoming_birthdays(users):
    date_format = "%Y.%m.%d"
    result = []
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], date_format).date()
        birthday_this_year = date(today.year, birthday.month, birthday.day)
        birthday_next_year = date(today.year + 1, birthday.month, birthday.day)
        delta = (birthday_this_year - today).days
        delta_next = (birthday_next_year - today).days
        if 0 <= delta <= 7:
            result.append(
                {
                    "name": name,
                    "congratulation_date": birthday_this_year.strftime(date_format),
                }
            )
        elif 0 <= delta_next <= 7:
            result.append(
                {
                    "name": name,
                    "congratulation_date": birthday_next_year.strftime(date_format),
                }
            )
    return result


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Petro", "birthday": "1990.03.7"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
