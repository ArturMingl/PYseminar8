"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов
и директорий.
"""

import os
import json
import csv
import pickle

from NotDirError import NotDirError


def dir_info_to_file(directory: str, json_file_path: str, csv_file_path: str, pickle_file_path: str):
    if not os.path.exists(directory) or not os.path.isdir(directory):
        raise NotDirError

    result = []

    for root, dirs, files in os.walk(directory):
        total_size = sum(os.stat(os.path.join(root, file)).st_size for file in files)
        rel_path = os.path.relpath(root, directory)
        result.append({
            'path': rel_path,
            'types': 'directory',
            'size': total_size,
        })

        for file in files:
            file_path = os.path.join(directory, root, file)
            file_size = os.stat(file_path).st_size

            result.append({
                'path': os.path.join(rel_path, file),
                'types': 'file',
                'size': file_size,
            })

    with(
        open(json_file_path, 'w', encoding='utf-8') as jf,
        open(csv_file_path, 'w', newline='', encoding='utf-8') as cf,
        open(pickle_file_path, 'wb') as pf,
    ):
        json.dump(result, jf, ensure_ascii=False, indent=4)
        csv_writer = csv.writer(cf)
        csv_writer.writerows(result)
        pickle.dump(result, pf)


if __name__ == '__main__':
    directory = '/Users/adisc/PycharmProjects/PYseminar8'
    json_file_path = '/Users/adisc/PycharmProjects/PYseminar8/test_dir/task2_res.json'
    csv_file_path = '/Users/adisc/PycharmProjects/PYseminar8/test_dir/task2_res.csv'
    pickle_file_path = '/Users/adisc/PycharmProjects/PYseminar8/test_dir/task2_res.pickle'

    dir_info_to_file(directory, json_file_path, csv_file_path, pickle_file_path)
