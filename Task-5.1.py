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

def doc_owner(number):
    result = 'Документ не обнаружен'
    for doc in documents:
        if doc['number'] == number:
            result = f'Владелец документа: {doc["name"]}'
    return result

def doc_shelf(number):
    result = 'Документ не обнаружен'
    for shelf_number, docs in directories.items():
        for doc_number in docs:
            if doc_number == number:
                result = f'Номер полки: {shelf_number}'
    return result

def doc_app(number, doc_type, name, shelf):
    if shelf in directories.keys():
        documents.append({"type": doc_type, "number": number, "name": name})
        directories[shelf].append(number)
        print('Документ успешно добавлен')
    else:
        print('Такой полки не существует')

def doc_del(number):
    for i in range(len(documents)):
        if documents[i].get('number') == number:
            del documents[i]
            print('Документ удален')
            break

while True:
    user_command = input('Введите команду (p,s,l,a,d): ')

    if user_command == 'p':
        user_input = input('Введите номер документа: ')
        print(doc_owner(user_input))
    elif user_command == 's':
        user_input = input('Введите номер документа: ')
        print(doc_shelf(user_input))
    elif user_command == 'l':
        print('Список всех документов: ')
        for doc in documents:
            print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')
    elif user_command == 'a':
        number = input('Введите номер документа: ')
        doc_type = input('Введите тип документа: ')
        name = input('Введите имя владельца: ')
        shelf = input('Введите номер полки: ')
        doc_app(number, doc_type, name, shelf)
    elif user_command == 'd':
        number = input('Введите номер документа: ')
        for doc in documents:
            if doc['number'] == number:
                doc_del(number)
                break
        else:
            print('Документ не обнаружен')
    else:
        print('Недопустимая команда')
