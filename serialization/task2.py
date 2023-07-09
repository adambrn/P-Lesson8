""" Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
Распечатайте его как pickle строку. """

import csv
import pickle

def read_csv_as_pickle_string(csv_file):
    data = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Читаем заголовок

        for row in reader:
            data.append(row)

    pickle_string = pickle.dumps(data)
    return pickle_string

if __name__ == '__main__':
    pickle_string = read_csv_as_pickle_string('users1.csv')
    print(pickle_string)
