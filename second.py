import numpy as np
import random
import matplotlib.pyplot as plt
import time
import datetime
import csv
import json

def export_to_csv(array):
    headers = ['Имя', 'Фамилия', 'Дата рождения', 'Пол', 'Водитель', 'Адрес']
    with open('records.csv', 'w', encoding='cp1251', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        for record in array:
            writer.writerow([
                record['name'],
                record['surname'],
                record['birthday'],
                record['sex'],
                record['is_driver'],
                record['address']
            ])
    return 

def import_from_csv():
    with open('records.csv', mode='r', encoding='cp1251') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        next(reader)
        data = []

        for record in reader:
            rec = {}
            rec['name'] = record[0]
            rec['surname'] = record[1]
            rec['birthday'] = record[2]
            rec['sex'] = record[3]
            rec['is_driver'] = record[4] == True
            rec['address'] = record[5]
            data.append(rec)
    return data


def export_to_json(array):
    with open('records.json', mode='w', encoding='utf-8') as outfile:
        json.dump(array, outfile, ensure_ascii=False)
        outfile.close()
    return

def import_from_json():
    with open('records.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
        file.close()
        return data

'''
    Имя (Строка)
'''
def load_names(count = 1000):
    with open('lists/male_names_rus.txt', 'r', encoding='utf-8') as file:
        names = file.readlines()
        names = [name.strip() for name in names]
        file.close()
        return random.choices(names, k=count)

'''
    Фамилия (Строка)
'''
def load_surnames(count = 1000):
    with open('lists/male_surnames_rus.txt', 'r', encoding='utf-8') as file:
        surnames = file.readlines()
        surnames = [surname.strip() for surname in surnames]
        file.close()
        return random.choices(surnames, k=count)

'''
    Пол (Строка)
'''
def get_rand_sex():
    options = ['M', 'F']
    return random.choice(options)

'''
    Наличие водительского удостоверения
'''
def get_rand_boolean():
    return random.choice([True, False])


def get_rand_birthdates(count = 1000):
    current_time = datetime.datetime.now()
    shift = datetime.timedelta(days=365 * 15)
    # Среднее значение для Unix-времени (20 леи назад)
    mean_unixtime = (current_time-shift).timestamp()  
    # Отклонение - 10 лет
    std_dev_unixtime = 60 * 60 * 24 * 30 * 12 * 10
    # Сформировали список с датами в формате unixtime
    # по нормальному распределение
    random_unixtime = np.random.normal(mean_unixtime, std_dev_unixtime, count)
    random_dates = [datetime.date.fromtimestamp(random_unixtime) for random_unixtime in random_unixtime]
    return random_dates

'''
    Адрес:
        город,
        улица,
        дом,
        квартира
'''
def get_rand_address():
    address = []
    cities = ['Астрахань', 'Архангельск', 'Барнаул', 'Белгород', 'Владимир', 'Воронеж', 'Грозный',
              'Гатчина', 'Дмитров', 'Домодедово', 'Екатеринбург', 'Ёлабуга', 'Железногорск', 'Жуковский',
              'Зеленоград', 'Златоуст', 'Иваново', 'Ижевск', 'Казань', 'Краснодар', 'Липецк']
    
    streets = ['Арбатская улица', 'Большая Дмитровка', 'Варварка улица', 'Гагаринская улица', 'Долгоруковская улица',
               'Елагинский проспект', 'Ёлочная улица', 'Живописная улица', 'Зубовская улица', 'Ильинка улица',
               'Красная площадь', 'Ленинградский проспект', 'Мясницкая улица', 'Невский проспект', 'Охотный ряд',
               'Пресненская набережная', 'Рублёвское шоссе', 'Садовое кольцо', 'Тверская улица', 'Улица Красная',
               'Фрунзенская набережная', 'Хохловская площадь', 'Цветной бульвар', 'Чистые пруды', 'Шоссе Энтузиастов',
               'Щукинская улица', 'Южная улица', 'Якиманка улица']
    address.append(random.choice(cities))
    address.append(random.choice(streets))
    address.append(np.random.randint(1, 100))
    address.append(np.random.randint(1, 100))
    return address


'''
    Сформировать случайные записи
'''
def create_rand_record(count = 50):
    names_list = load_names(count)
    surnames_list = load_surnames(count)
    birthdates_list = get_rand_birthdates(count)
    records = []
    for index, record in enumerate(range(1, count)):
        rec = {}
        rec['name'] = names_list[index]
        rec['surname'] = surnames_list[index]
        rec['birthday'] = birthdates_list[index].isoformat()
        rec['sex'] = get_rand_sex()
        rec['is_driver'] = get_rand_boolean()
        rec['address'] = get_rand_address()
        records.append(rec)

    for rec in records:
        print(rec, sep='\n')
    return records


def create_hist(records):
    today = datetime.date.today()
    birthdays = [item['birthday'] for item in records]
    
    ages = []
    for birthday in birthdays:
        age =(today - datetime.datetime.strptime(birthday, '%Y-%m-%d').date()).days // 365
        ages.append(age)

    plt.hist(ages, bins = range(min(ages), max(ages) + 2))
    plt.xlabel('Возраст')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()
    return 


def get_age(birthday):
    today = datetime.date.today()
    birthdate = datetime.datetime.strptime(birthday, '%Y-%m-%d').date()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

'''
    Оставить только записи, имеющие
    возраст >= 18 лет
'''
def filter_records(records):
    result = []
    for record in records:
        if get_age(record['birthday']) >=18:
            result.append(record)
    return result

def second_practice():
    # records = create_rand_record(1000)
    # print(records[:25])
    # export_to_json(records)
    records = import_from_json()
    create_hist(records)
    records = filter_records(records)
    # random_records = create_rand_record(50)
    # export_to_json(random_records)

    # data = import_from_csv()
    # for rec in random_records:
    #     print(rec)
    create_hist(records)
    # filter_records(random_records)
    # data = import_from_json()
    # print(data)

    return