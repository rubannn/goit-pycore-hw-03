"""
У вашій компанії ведеться активна маркетингова кампанія за допомогою SMS-розсилок.
Для цього ви збираєте телефонні номери клієнтів із бази даних, але часто стикаєтеся
з тим, що номери записані у різних форматах. Наприклад:

"    +38(050)123-32-34"
"     0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11   "
"""

# 1(+) + 3(code) + 2(operator) + 7(number)

import re


def normalize_phone(phone_number: str) -> str:
    clear_phone_number = re.sub(r"[^0-9+]", "", phone_number)
    # if number is correct - return
    if re.fullmatch(r"\+380\d{9}", clear_phone_number):
        return clear_phone_number
    # else cut from end only 9 symbols and add code +380
    return f"+380{clear_phone_number[-9:]}"


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

standard = [
    "+380671234567",
    "+380952345678",
    "+380441234567",
    "+380501234567",
    "+380501233234",
    "+380503451234",
    "+380508889900",
    "+380501112222",
    "+380501112211",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers[:]]
if sanitized_numbers == standard:
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
else:
    print("Невірна відповідь")
