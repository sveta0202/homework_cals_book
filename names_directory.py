# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
from typing import List

def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
    return []

def show_data(data: list):
    for line in data:
        print(line)

def Comments():
    pass
    # with open('note.txt', 'r', encoding='utf-8') as f:
    # lines = f.readlines()
    # for line in lines:
    # print(line)
    # FileNotFoundError
    # try:
    # # print('открытие файла')
    # with open('note.txt', 'r', encoding='utf-8') as f:
    # lines = f.readlines()
    # for line in lines:
    # print(line)
    # except FileNotFoundError as err:
    # print('файла нет. Сначала введите данные\n')
    # else:
    # print('else')
    # finally:
    # print('finally')

def save_data(file):
    print('Введите данные контакта:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')

    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')

def search_data(contacts: List[str]):
    print("Найти по: 1-фамилии, 2-имени, 3-номеру телефона.")
    answer_two = int(input())
    if answer_two == 1:
        search_str = input('Введите фамилию для поиска: ')
        founded = []
        # search_idx
        for contact in contacts:
            if search_str.lower() in contact.split(', ')[1].lower():
                founded.append(contact)
        return founded
    
    if answer_two == 2:
        search_str = input('Введите имя для поиска: ')
        founded = []
        for contact in contacts:
            if search_str.lower() in contact.split(', ')[0].lower():
                founded.append(contact)
        return founded
    
    if answer_two == 3:
        search_str = input('Введите номер телефона для поиска: ')
        founded = []
        for contact in contacts:
            if search_str.lower() in contact.split(', ')[3].lower():
                founded.append(contact)
        return founded
    
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def delete_data(file):
    print('Введите данные контакта, который хотите удалить:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    text = (f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')
    lines = [line for line in lines if text not in line]
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
def rename_data(file, data):
    print('Введите данные контакта, который хотите изменить:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    text = (f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')
    lines = [line for line in lines if text not in line]
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print('Введите новые данные контакта:')
    first_name = input('Введите новое имя: ')
    last_name = input('Введите новую фамилию: ')
    patronymic = input('Введите новое отчество: ')
    phone_number = input('Введите новый номер телефона: ')

    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')

# ---------------------------------------------------------------      
def main():
    file_name = 'note.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - удалить запись')
        print('5 - изменить запись')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
            data = read_file(file_name)
            delete_data(file_name)
        elif answer == '5':
            data = read_file(file_name)
            rename_data(file_name, data)
        else:
            print('Такой команды нет в меню, повторите попытку.')

if __name__ == '__main__':
    main()