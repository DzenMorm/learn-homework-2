"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import timedelta, datetime

def print_days():
    yesteday = (datetime.now() - timedelta(1)).strftime('%d-%m-%Y')
    today = (datetime.now()).strftime('%d-%m-%Y')
    ago_30_days = (datetime.now() - timedelta(30)).strftime('%d-%m-%Y')
    print(f"Вчера было {yesteday}")
    print(f"Сегодня {today}")
    print(f"30 дней назад было {ago_30_days}")


def str_2_datetime(date_string):
    date_dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return date_dt


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
