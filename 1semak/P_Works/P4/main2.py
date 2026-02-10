import json
import csv
import os

# Имена файлов
json_file = 'test_json.json'
csv_file = 'employees_with_salary.csv'

# 1. Читаем JSON-файл
try:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Ошибка: файл {json_file} не найден.")
    exit()
except json.JSONDecodeError as e:
    print(f"Ошибка чтения JSON: {e}")
    exit()

# Проверяем, что все нужные ключи есть в JSON
required_keys = ['Имя', 'Возраст', 'Город']
if not all(key in data for key in required_keys):
    print(f"В JSON отсутствуют обязательные поля: {required_keys}")
    exit()

# 2. Формируем новую строку с дополнительными полями
new_row = {
    'Имя': data['Имя'],
    'Возраст': data['Возраст'],
    'Город': data['Город'],
    'Должность': 'Стажёр',
    'Зарплата': 50000
}

# 3. Определяем, существует ли CSV-файл
file_exists = os.path.isfile(csv_file)

# 4. Открываем CSV для записи (добавления)
with open(csv_file, 'a', newline='', encoding='utf-8') as f:
    fieldnames = ['Имя', 'Возраст', 'Город', 'Должность', 'Зарплата']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # Если файла нет — пишем заголовки
    if not file_exists:
        writer.writeheader()

    # Пишем новую строку
    writer.writerow(new_row)

print(f"Данные успешно добавлены в {csv_file}.")