""" Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться. """

import json
import os

def add_user_to_json(file_path):
    data = {}

    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)

    while True:
        name = input("Введите имя пользователя (или 'exit' для выхода): ")
        if name == 'exit':
            break
        identifier = input("Введите личный идентификатор пользователя: ")
        while identifier in {key for level in data.values() for key in level}:
            identifier = input("Идентификатор уже существует. Пожалуйста, введите уникальный идентификатор: ")
            
        access_level = 0
        while int(access_level) < 1 or int(access_level) > 7:
            access_level = input("Введите уровень доступа (от 1 до 7): ")

        user = {identifier:name}
        data.setdefault(access_level, {}).update(user)


        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print("Пользователь успешно добавлен в JSON файл.")

if __name__ == '__main__':
    add_user_to_json('users.json')
