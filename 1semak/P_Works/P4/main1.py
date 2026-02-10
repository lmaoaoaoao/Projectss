import json


with open('country.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


data['язык'] = 'французский'


with open('country.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
