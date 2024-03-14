"""
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""

import json
import os

from my_package.NotDirError import NotDirError


def txt_to_json(txt_path: str, json_path: str):
    if not os.path.exists(txt_path):
        raise NotDirError

    with open(txt_path, 'r', encoding='utf-8') as f:
        data = []
        for line in f:
            data.append(line.capitalize())
        data = ''.join(data)

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    json_file_path = '/Users/adisc/PycharmProjects/PYseminar8/test_dir/task1_result.json'
    txt_file_path = '/Users/adisc/PycharmProjects/PYseminar8/test_dir/sem7_result.txt'

    txt_to_json(txt_file_path, json_file_path)
