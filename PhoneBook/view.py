# пользовательский интерфейс
def welcome():
    print('Телефонная книга')
    book = int(input('Меню: \n\
    1 - Добавить абонента\n\
    2 - Поиск абонента\n\
    3 - Показать всех абонентов\n\
    4 - Выход\n\
Выберите пункт: '))
    print()
    return book

def output():
    out = int(input('Вывод данных: \n\
        1 - в одну линию \n\
        2 - на каждой строке \n\
        Ваш выбор: '))
    print()
    return out
