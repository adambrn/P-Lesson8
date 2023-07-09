""" Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. 
Для тестированию возьмите pickle версию файла из предыдущей задачи. 
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла. """

import pickle
import csv

def convert_pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as file:
        data = pickle.load(file)

    if data:
        keys = data[0].keys()  
        # print(keys)
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()

            writer.writerows(data)

        print(f"Файл {pickle_file} успешно преобразован в {csv_file}.")
    else:
        print(f"Файл {pickle_file} не содержит данных.")

if __name__ == '__main__':
    convert_pickle_to_csv('users1.pickle', 'users1.csv')
