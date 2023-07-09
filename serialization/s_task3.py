# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import csv
import json

def save_as_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Access Level'])

        for access_level, user_data in data.items():
            for identifier, user in user_data.items():
                row = [identifier, user, access_level]
                writer.writerow(row)

    print("Файл успешно сохранен в формате CSV.")

if __name__ == '__main__':
    save_as_csv('users.json', 'users.csv')
