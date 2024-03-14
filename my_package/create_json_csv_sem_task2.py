"""
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.

task3. Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""

import json
import os


def read_json(json_path: str):
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as json_file:
            access_dict = json.load(json_file)
    else:
        access_dict = {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}}
    return access_dict


def write_json(json_path: str, csv_path: str):
    access_dict = read_json(json_path)
    while True:
        name = input("Введите имя: ")
        while True:
            flag = False
            ident = input("Введите ID: ")
            for keys, values in access_dict.items():
                if ident in values.keys():
                    print("Такой ID уже есть.")
                    flag = True
            if not flag:
                break
        while True:
            access_level = input("Веедите уровень доступа: ")
            if "0" < access_level < "8":
                break

        access_dict[access_level][ident] = name
        x = input("Выйти из цикла? y/n\n")
        if x == 'y':
            break

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(access_dict, json_file, indent=4, ensure_ascii=False)
    with open(csv_path, 'w', encoding='utf-8') as csv_file:
        for key, value in access_dict.items():
            for key2, value2 in value.items():
                csv_file.write(f'{key},{key2},{value2}\n')


if __name__ == "__main__":
    json_path = '/Users/adisc/PycharmProjects/PYseminar8/test_dir/task2_result.json'
    csv_path = '/Users/adisc/PycharmProjects/PYseminar8/test_dir/task2_result.csv'
    write_json(json_path, csv_path)
