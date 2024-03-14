"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""

import json
import os


def csv_to_json(csv_name: str, json_name: str):
    if not os.path.exists(csv_name):
        raise FileNotFoundError('нет файла')
    with open(csv_name, 'r', encoding='utf-8') as f:
        with open(json_name, 'a', encoding='utf-8') as f2:
            for line in f:
                level, ident, name = line.strip().split(',')
                ident = f'{int(ident):010d}'
                name = name.title()
                hash_name = hash(name + ident)
                my_dict = {level: [ident, name, hash_name]}
                print(json.dumps(my_dict), file=f2)


if __name__ == '__main__':
    csv_to_json('task2_result.csv', 'task4_result.json')