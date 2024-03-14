"""
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""

import pickle
import os


def pikle_to_csv(pikle_path: str, csv_path: str, dict_list: list[{dict}]):
    with open(pikle_path, 'wb') as f:
        pickle.dump(dict_list, f)
    with open(pikle_path, 'rb') as f:
        data = pickle.load(f)
    with open(csv_path, 'w', encoding='utf-8') as f:
        for my_dict in dict_list:
            for key, value in my_dict.items():
                print(f'{key}, {value}', file=f)

if __name__ == '__main__':
    dict_list = [{1: 3}, {32: 'fds'}, {4: 5343}]
    pickle_path = '../dict_list.pickle'
    csv_path = '../dict_list.csv'

    pikle_to_csv(pickle_path, csv_path, dict_list)
