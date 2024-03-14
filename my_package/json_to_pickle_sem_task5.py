"""
Напишите функцию, которая ищет json файлы в указанной директории
и сохраняет их содержимое в виде одноимённых pickle файлов.
"""

import json
import os
import pickle

from my_package import NotDirError


def json_to_pickle(dir_name: str):
    if not os.path.exists(dir_name) or not os.path.isdir(dir_name):
        raise NotDirError
    for file_name in os.listdir(dir_name):
        if file_name.endswith('.json'):
            with open(os.path.join(dir_name, file_name), 'r', encoding='utf-8') as f:
                data = json.load(f)
            with open(os.path.join(dir_name, file_name.replace('.json', '.pickle')), 'wb') as f:
                pickle.dump(data, f)


if __name__ == '__main__':
    json_to_pickle('../test_dir')
