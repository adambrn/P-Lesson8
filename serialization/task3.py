import os
import csv
import json
import pickle

def get_directory_size(directory):
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))
    
    return total_size

def save_directory_info(directory=None):
    if not directory:
        directory = os.getcwd()
   
    result = []

    for root, dirs, files in os.walk(directory):

        dir_info = {
            'obj': os.path.basename(root),
            'parent': os.path.basename(os.path.dirname(root)),
            'obj_type': 'Directory',
            'size': get_directory_size(root)
        }

        result.append(dir_info)

        for file in files:

            file_info = {
                'obj': file,
                'parent': os.path.basename(root),
                'obj_type': 'File',
                'size': os.path.getsize(os.path.join(root, file))
            }

            result.append(file_info)

    # CSV файл
    csv_file = os.path.join(directory, 'result.csv')
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['obj', 'parent', 'obj_type', 'size'])

        for item in result:
            writer.writerow([item['obj'], item['parent'], item['obj_type'], item['size']])

    # JSON файл
    json_file = os.path.join(directory, 'result.json')
    with open(json_file, 'w') as file:
        json.dump(result, file, indent=4)

    # pickle файл
    pickle_file = os.path.join(directory, 'result.pickle')
    with open(pickle_file, 'wb') as file:
        pickle.dump(result, file)

    print(f"Результаты обхода директории сохранены в файлы: {csv_file}, {json_file}, {pickle_file}.")


if __name__ == '__main__':
    save_directory_info()
