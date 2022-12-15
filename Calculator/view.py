def view_data(data, title):
    print(f'{title} = {data}')

def choice_number_class():
    return int(input('Введите 0 для работы с рациональными числами или 1 - с комплексными: '))

def get_value():
    return float(input('Значение = '))


def get_operation():
    print("Выберите операцию: + - * / ")
    return input('операция = ')