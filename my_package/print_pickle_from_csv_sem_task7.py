"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
"""

import pickle


def print_pickle_from_csv(csv_path):
    with open(csv_path, 'r', encoding='utf-8') as f:
        data = []
        for line in f:
            key, value = line.strip().split(',')
            data.append({key: value})
        print(pickle.dumps(data))


if __name__ == '__main__':
    csv_path = '../dict_list.csv'
    print_pickle_from_csv(csv_path)
