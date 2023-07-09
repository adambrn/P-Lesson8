# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноименных pickle файлов.

import os
import json
import pickle

def convert_json_to_pickle(directory=None):
    if not directory:
        directory = os.getcwd()

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            json_file = os.path.join(directory, filename)
            pickle_file = os.path.join(directory, filename.replace('.json', '.pickle'))

            with open(json_file, 'r') as jf, open(pickle_file, 'wb') as pf:
                data = json.load(jf)
                pickle.dump(data, pf)

            print(f"Файл {json_file} успешно преобразован в {pickle_file}.")

if __name__ == '__main__':
    convert_json_to_pickle()  
    #convert_json_to_pickle('C:/GB/')  
