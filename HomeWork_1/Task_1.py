# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def weeks_day(number):
    while number < 1 or number > 7:
        number = int(input(f'{number} - некорректное число. Введите число от 1 до 7: '))
    if 1 <= number <= 5:
        return (f'{number} -> нет')
    elif number == 6 or number == 7:
        return (f'{number} -> да')

day = int(input('Введите номер дня недели: '))

print(weeks_day(day))
