import csv
import json


test = [
    ['Имя','Возраст','Город',],
    ['Анна', 30,'Москва',],
    ['Михаил', 24,'Питер',]
]



with open ('text_csv','w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(test)


with open ('text_csv','r',encoding='utf-8') as file:
    reader = csv.reader(file)
    for row_num, row in enumerate(reader,1):
        print(f'Строка {row_num}: {row}')
        print(type(row))

print('\n\n')




with open ('text_csv','r',encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f'{row['Имя']}, Возраст: {row['Возраст']}, Город: {row['Город']}')
        print(f"  Тип: {type(row)}")
        
print('\n\n')
'''



'''
employees = [
    {'Имя': 'Анна', 'Возраст': '28', 'Город': 'Москва', 'Должность': 'Разработчик'},
    {'Имя': 'Иван', 'Возраст': '34', 'Город': 'Санкт-Петербург', 'Должность': 'Менеджер'},
    {'Имя': 'Мария', 'Возраст': '25', 'Город': 'Казань', 'Должность': 'Дизайнер'}
]


OUTUP_FILE='csv_text'

fieldnames=['Возраст','Имя','Город','Должность']


with open (OUTUP_FILE,'w',newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees)



test_data_csv={'Имя': 'Анна', 'Возраст': '28', 'Город': 'Москва', 'Должность': 'Разработчик'}

with open ('json_file','w', encoding='utf-8') as file:
    json.dump(test_data_csv, file, ensure_ascii=False, indent = 2)


with open ('json_file','r',encoding='utf-8') as file:
    reader=json.load(file)
    print(f'Данные {reader}')
    print(f'Тип {type(reader)}')





