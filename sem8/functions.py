def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'rt', encoding='utf-8') as book:
        data = book.read()
    print(data)


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    print(data)
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find))


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    data_list = []
    for contact in book:
        if info in contact:
            data_list.append(contact)
    print(data_list)
    if len(data_list) == 1:
        return data_list[0]
    elif len(data_list) > 1:
        data = input('Введите уточненные данные для поиска: ')
        for contact in data_list:
            if data in contact:
                return contact
    return 'Совпадений не найдено'


def change_data():
    """Изменяет найденные данные в файла"""
    data_change = input('Введите данные для изменения: ')
    data_find = input('Введите данные для поиска: ')
    with open('book.txt', 'rt', encoding='utf-8') as file:
        data_read = file.read()
    data_to_remove = search(data_read, data_find)
    if data_to_remove:
        data_replace = data_read.replace(data_to_remove, data_change)
        with open('book.txt', 'wt', encoding='utf-8') as book:
            book.write(data_replace)
    else:
        print(data_to_remove)


def remove_data():
    """Удаляет найденные данные в файле"""
    data_remove = input('Введите данные для удаления: ')
    with open('book.txt', 'r', encoding='utf-8') as file_read:
        data_read = file_read.read()
    data_to_remove = search(data_read, data_remove)
    if data_to_remove:
        data_replace = data_read.replace(data_to_remove, " ")
        with open('book.txt', 'w', encoding='utf-8') as file_write:
            file_write.write(data_replace)







