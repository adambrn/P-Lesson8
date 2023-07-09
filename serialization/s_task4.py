""" Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции. """

import csv
import json

def process_csv_to_json(csv_file, json_file):
    data = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        _ = next(reader)  # Убираем заголовок

        for row in reader:
            # Создание словаря с данными
            identifier = row[0].zfill(10)
            name = row[1].capitalize()
            user_data = {
                'id': identifier,
                'name': name,
                'access_level': int(row[2]),
                'hash': hash(f"{name}{identifier}")
            }

            data.append(user_data)

    with open(json_file, 'w') as file:
            json.dump(data, file)
          

    print("Данные успешно сохранены в формате JSON.")

if __name__ == '__main__':
    process_csv_to_json('users.csv', 'users1.json')
