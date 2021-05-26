"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

name_age_job_dict = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Коля', 'age': 34, 'job': 'Doctor'}, 
    {'name': 'Марк', 'age': 45, 'job': 'Writer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]


def main(dict_for_csv):
    with open("my_text.csv", "w", encoding="utf-8") as f:
        fields = ["name", "age", "job"]
        writer = csv.DictWriter(f, fields, delimiter=";")
        writer.writeheader()
        writer.writerows(name_age_job_dict)


if __name__ == "__main__":
    main(name_age_job_dict)
