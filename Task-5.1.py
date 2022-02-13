documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
        }

print('Список команд:\np - поиск владельца по номеру документа\n\
s - поиск полки по номеру документа\nl - вывести список всех документов\na - добавить новый документ\nd - удалить документ\n\
m - переместить документ\nas - добавить новую полку\nq - выйти из программы')

def show_doc_owner(number):
    result = 'Документ не обнаружен'
    for doc in documents:
        if doc['number'] == number:
            result = f'Владелец документа: {doc["name"]}'
    return result

def show_doc_shelf(number):
    result ='Документ не обнаружен'
    for shelf_number, docs in directories.items():
        for doc_number in docs:
            if doc_number == number:
                result = f'Номер полки: {shelf_number}'
    return result

def append_doc(number, doc_type, name, shelf):
    if shelf in directories.keys():
        documents.append({"type": doc_type, "number": number, "name": name})
        directories[shelf].append(number)
        print('Документ успешно добавлен')
    else:
        print('Такой полки не существует')

def delite_doc(number):
    for doc in documents:
        if doc['number'] == number:
            for i in range(len(documents)):
                if documents[i].get('number') == number:
                    del documents[i]
                    for val in directories.values():
                        val.remove(number)
                        print('Документ удален')
                        return
    else:
        print('Документ не обнаружен')

def move_doc(number, shelf):
    for doc in documents:
        if doc['number'] == number:
            if shelf in directories.keys():
                for val in directories.values():
                    val.remove(number)
                    directories[shelf].append(number)
                    print('Документ перемещен')
                    return
            else:
                print('Такой полки не существует')
                return
    else:
        print('Документ не обнаружен')

def add_shelf(shelf):
    if shelf in directories.keys():
        print('Такая полка уже есть')
    else:
        directories[shelf] = []
        print('Полка успешно добавлена')
        return

while True:
    user_command = str.lower(input('\nВведите команду: '))

    if user_command == 'p':
        user_input = input('Введите номер документа: ')
        print(show_doc_owner(user_input))
    elif user_command == 's':
        user_input = input('Введите номер документа: ')
        print(show_doc_shelf(user_input))
    elif user_command == 'l':
        print('Список всех документов: ')
        for doc in documents:
            print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')
    elif user_command == 'a':
        number = input('Введите номер документа: ')
        doc_type = input('Введите тип документа: ')
        name = input('Введите имя владельца: ')
        shelf = input('Введите номер полки: ')
        append_doc(number, doc_type, name, shelf)
    elif user_command == 'd':
        number = input('Введите номер документа: ')
        delite_doc(number)
    elif user_command == 'm':
        number = input('Введите номер документа: ')
        shelf = input('Введите номер полки: ')
        move_doc(number, shelf)
    elif user_command == 'as':
        shelf = input('Введите номер полки: ')
        add_shelf(shelf)
    elif user_command == 'q':
        print('Программа закрыта')
        break
    else:
        print('Недопустимая команда!')
